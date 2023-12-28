#!/usr/bin/env python3

import io
import csv
import uvicorn
from datetime import datetime
from fastapi import FastAPI, Request, Response
import matplotlib.pyplot as plt

class Product:
	"""Product holds all the values related to each product in the data set."""
	def __init__(self, factory: str, area: str, date: str, product_code: str):
		self.factory = factory
		self.area = area
		self.date = datetime.strptime(date, r"%Y-%m-%d %H:%M:%S.%f")
		self.product_code = product_code

	def __str__(self):
		return f"{{{self.factory}, {self.area}, {self.date.strftime(r'%Y-%m-%d %H:%M:%S.%f')}, {self.product_code}}}"

class Pool:
	"""Pool manages the data pool exporting all methods useful for the data manipulation."""
	def __init__(self, products: list):
		self.products = products

	def __iter__(self):
		self.pos = 0
		return self

	def __next__(self) -> Product:
		if self.pos < len(self.products):
			ret = self.products[self.pos]
			self.pos += 1
			return ret
		raise StopIteration

	@staticmethod
	def load_csv(path: str):
		"""load_csv reads a CSV file at the provided path and returns a new Pool object with the parsed data"""
		products = []
		with open(path) as f:
			for row in csv.DictReader(f):
				products.append(Product(row["factory"], row["area"], row["date"], row["product_code"]))
		return Pool(products)

	def day(self, day: datetime = datetime.today().day):
		"""day returns a new Pool object with the products filtered by day"""
		return Pool(list(filter(lambda p: p.date.day == day, self.products))) if day else self

	def month(self, month: datetime = datetime.today().month):
		"""month returns a new Pool object with the products filtered by month"""
		return Pool(list(filter(lambda p: p.date.month == month, self.products))) if month else self

	def year(self, year: datetime = datetime.today().year):
		"""year returns a new Pool object with the products filtered by year"""
		return Pool(list(filter(lambda p: p.date.year == year, self.products))) if year else self

	def range(self, start: datetime, end: datetime):
		"""range returns a new Pool object with the products produced in the provided range"""
		return Pool(list(filter(lambda p: p.date.date() >= start.date() and p.date.date() <= end.date(), self.products)))

	def area(self, area: str):
		"""area returns a new Pool object with the products produced in the provided area"""
		return Pool(list(filter(lambda p: p.area == area, self.products))) if area else self

	def _get_num_days(self) -> int:
		"""_get_num_days returns the number of days in the pool"""
		# Use a newly created datetime object to filter out not needed data.
		return len(set(datetime(p.date.year, p.date.month, p.date.day).date() for p in self.products))

	def _get_num_months(self) -> int:
		"""_get_num_months returns the number of months in the pool"""
		return len(set(datetime(p.date.year, p.date.month, 1).date() for p in self.products))

	def _add_stats(self, data: dict) -> None:
		"""_add_stats adds additional statistics to the kpi data dictionary"""
		return {
			area: {
				"kpi": len(codes),
				"daily_average_kpi": len(codes) / self._get_num_days(),
				"product_codes": codes
			}
			for area, codes in data.items()
		}

	def kpi(self) -> dict:
		"""kpi returns a dictionary containing the KPI data of the Pool object"""
		d = {}

		for p in self.products:
			# Set d[p.area] to an empty dictionary and d[p.area][p.product_code] to 0 by default.
			d.setdefault(p.area, {}).setdefault(p.product_code, 0)
			d[p.area][p.product_code] += 1
		return self._add_stats(d)

	def year_avg_kpi(self, year: int = datetime.today().year) -> dict:
		"""year_avg_kpi returns a dictionary containing the KPI value aggregated by year as the average value of monthly KPI values"""
		d = {}
		merge_and_sum = lambda d1, d2: {k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2)}

		for m in range(1, 13):
			for area, data in self.month(m).kpi().items():
				a = d.setdefault(area, {})
				a["kpi"] = a.get("kpi", 0) + data["daily_average_kpi"]
				# Merge and sum the dictionary with the total of products with the current month one.
				a["product_codes"] = merge_and_sum(a.get("product_codes", {}), data["product_codes"])

		months = self._get_num_months()
		return {
			area: {
				"kpi": d[area]["kpi"]/months,
				"plot_url": f"/kpi/year/plot/{area}/{year}",
				"product_codes": d[area]["product_codes"]
			}
			for area in d
		}

	def year_plot(self, area: str) -> bytes:
		"""year_plot returns the plot of the monthly KPI average as PNG encoded bytes"""
		vals = {}
		tmp = self.area(area)

		for m in range(1, 13):
			for a, d in tmp.month(m).kpi().items():
				vals[m] = d["daily_average_kpi"]

		# Create two tuples x and y with respectively the months in the x and the average KPIs in the y.
		x, y = zip(*vals.items())
		fig = plt.Figure()
		ax = fig.add_subplot(111)
		ax.bar(x, y)
		ax.set_xlabel("Month")
		ax.set_ylabel("Average KPI")
		ax.set_title(f"Monthly average KPI in {area} area")
		ax.set_xticks(x)

		buf = io.BytesIO()
		fig.savefig(buf, format="png")
		buf.seek(0)
		return buf.getvalue()


class QueryException(Exception):
	def __init__(self, msg):
		super().__init__(msg)

def is_date_valid(day: int, month: int, year: int) -> bool:
	try:
		datetime(year or datetime.today().year, month or 1, day or 1)
		return True
	except ValueError:
		return False

def parse_date_queries(query_params: Request.query_params) -> tuple:
	int_or_none = lambda i: int(i) if i else None

	try:
		day = int_or_none(query_params.get("day", None))
		month = int_or_none(query_params.get("month", None))
		year = int_or_none(query_params.get("year", None))
	except TypeError:
		raise QueryException("query parameters must be of integer type")

	if not is_date_valid(day, month, year):
		raise QueryException("invalid date provided")

	return (day, month, year)

def parse_range_queries(query_params) -> tuple:
	try:
		start = datetime.strptime(query_params.get("start", None), r"%Y-%m-%d")
		end = datetime.strptime(query_params.get("end", None), r"%Y-%m-%d")
	except Exception:
		raise QueryException("invalid range, date must respect the format YYYY-MM-DD")
	return (start, end)

def ok(data) -> dict:
	return {"ok": True, "data": data}

def error(err: Exception) -> dict:
	return {"ok": False, "error": str(err)}

app = FastAPI()
data = Pool.load_csv("data.csv")

@app.get("/")
def data_endpoint(req: Request):
	try:
		day, month, year = parse_date_queries(req.query_params)
		return ok(data.year(year).month(month).day(day).products)
	except Exception as e:
		return error(e)

@app.get("/range")
def range_endpoint(req: Request):
	try:
		start, end = parse_range_queries(req.query_params)
		return ok(data.range(start, end).products)
	except Exception as e:
		return error(e)

@app.get("/kpi")
def kpi_endpoint(req: Request):
	try:
		day, month, year = parse_date_queries(req.query_params)
		return ok(data.year(year).month(month).day(day).kpi())
	except Exception as e:
		return error(e)

@app.get("/kpi/year")
def default_year_kpi_endpoint():
	return year_kpi_endpoint()

@app.get("/kpi/year/{year}")
def year_kpi_endpoint(year=datetime.today().year):
	try:
		return ok(data.year(int(year)).year_avg_kpi(int(year)))
	except Exception as e:
		return error(e)

@app.get("/kpi/year/plot/{area}")
def default_year_kpi_plot(area=""):
	return year_kpi_plot(area)

@app.get("/kpi/year/plot/{area}/{year}")
def year_kpi_plot(area="", year=datetime.today().year):
	try:
		return Response(content=data.year(int(year)).year_plot(area.upper()), media_type="image/png")
	except Exception as e:
		return error(e)

@app.get("/kpi/range")
def kpi_range_endpoint(req: Request):
	try:
		start, end = parse_range_queries(req.query_params)
		return ok(data.range(start, end).kpi())
	except Exception as e:
		return error(e)

if __name__ == "__main__":
	uvicorn.run(app, host="localhost", port=8080)
