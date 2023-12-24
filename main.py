#!/usr/bin/env python3

import csv
from datetime import datetime
from fastapi import FastAPI, Request

class Product:
	"""Product holds all the values related to each product in the data set."""
	def __init__(self, factory, area, date, product_code):
		self.factory = factory
		self.area = area
		self.date = datetime.strptime(date, r"%Y-%m-%d %H:%M:%S.%f")
		self.product_code = product_code

	def __str__(self):
		return f"{{{self.factory}, {self.area}, {self.date.strftime(r'%Y-%m-%d %H:%M:%S.%f')}, {self.product_code}}}"


class Pool:
	"""Pool manages the data pool exporting all methods useful for the data manipulation."""
	def __init__(self, products):
		self.products = products

	def __iter__(self):
		self.pos = 0
		return self

	def __next__(self):
		if self.pos < len(self.products):
			ret = self.products[self.pos]
			self.pos += 1
			return ret
		raise StopIteration

	@staticmethod
	def load_csv(path):
		products = []
		with open(path) as f:
			for row in csv.DictReader(f):
				products.append(Product(row["factory"], row["area"], row["date"], row["product_code"]))
		return Pool(products)

	def day(self, day=datetime.today().day):
		"""day returns a new Pool object with the products filtered by day"""
		return Pool(list(filter(lambda p: p.date.day == day, self.products))) if day else self

	def month(self, month=datetime.today().month):
		"""month returns a new Pool object with the products filtered by month"""
		return Pool(list(filter(lambda p: p.date.month == month, self.products))) if month else self

	def year(self, year=datetime.today().year):
		"""year returns a new Pool object with the products filtered by year"""
		return Pool(list(filter(lambda p: p.date.year == year, self.products))) if year else self

	def range(self, start, end):
		"""range returns a new Pool object with the products produced in the provided range"""
		return Pool(list(filter(lambda p: p.date.date() >= start.date() and p.date.date() <= end.date(), self.products)))

	# Returns the number of days in the pool.
	def _get_num_days(self):
		return len(set(datetime(p.date.year, p.date.month, p.date.day).date() for p in self.products))

	def _add_stats(self, data):
		d = {}
		for area, codes in data.items():
			d[area] = {"kpi": len(codes), "average_kpi": len(codes) / self._get_num_days(), "codes": codes}
		return d

	def kpi(self):
		d = {}

		for p in self.products:
			if p.area not in d:
				d[p.area] = {}

			if p.product_code not in d[p.area]:
				d[p.area][p.product_code] = 1
			else:
				d[p.area][p.product_code] += 1

		return self._add_stats(d)

class QueryException(Exception):
	def __init__(self, msg):
		super().__init__(msg)

def is_date_valid(day, month, year):
	if not day:
		day = 1
	if not month:
		month = 1
	if not year:
		year = datetime.today().year

	try:
		datetime(year, month, day)
	except ValueError:
		return False
	return True

def parse_date_queries(query_params):
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

def parse_range_queries(query_params):
	try:
		start = datetime.strptime(query_params.get("start", None), r"%Y-%m-%d")
		end = datetime.strptime(query_params.get("end", None), r"%Y-%m-%d")
	except Exception:
		raise QueryException("invalid range, date must respect the format YYYY-MM-DD")
	return (start, end)

def ok(data):
	return {"ok": True, "data": data}

def error(err):
	return {"ok": False, "error": str(err)}

app = FastAPI()
data = Pool.load_csv("data.csv")

@app.get("/")
def data_endpoint(req: Request):
	try:
		day, month, year = parse_date_queries(req.query_params)
	except Exception as e:
		return error(e)
	return ok(data.year(year).month(month).day(day).products)

@app.get("/range")
def data_endpoint(req: Request):
	try:
		start, end = parse_range_queries(req.query_params)
	except Exception as e:
		return error(e)
	return ok(data.range(start, end).products)

@app.get("/kpi")
def kpi_endpoint(req: Request):
	try:
		day, month, year = parse_date_queries(req.query_params)
	except Exception as e:
		return error(e)
	return ok(data.year(year).month(month).day(day).kpi())

@app.get("/kpi/range")
def kpi_range_endpoint(req: Request):
	try:
		start, end = parse_range_queries(req.query_params)
	except Exception as e:
		return error(e)
	return ok(data.range(start, end).kpi())
