from pool import Pool
from datetime import datetime
from fastapi import FastAPI, Request, Response

class QueryException(Exception):
	def __init__(self, msg):
		super().__init__(msg)

app = FastAPI()
data = Pool.load_csv("data.csv")

def is_date_valid(day, month, year) -> bool:
	try:
		datetime(year or datetime.today().year, month or 1, day or 1)
		return True
	except ValueError:
		return False

def parse_date_queries(query_params) -> tuple:
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
