[![DeepSource](https://app.deepsource.com/gh/NicoNex/kpi-assignment.svg/?label=resolved+issues&show_trend=true&token=Jw4qv5Q_CmgK14F8VUTFO0Af)](https://app.deepsource.com/gh/NicoNex/kpi-assignment/)

# kpi-assignment

All endpoints return the following empty json when no data is available, this is to differenciate between an eventual 0 KPI and the lack of data in the dataset.
```json
{
	"ok": true,
	"data": {}
}
```

All endpoints include an "ok" field with a boolean value to make it straightforward to any front-end whether an exception has been raised, in that case the response will look like this:
```json
{
	"ok": false,
	"error": "the error message"
}
```
## Endpoints

### /
This endpoint shows the data in the dataset and accpepts any of the following query parameters of integer type:
- `day` to filter the dataset by day
- `month` to filter the dataset by month
- `year` to filter the dataset by year

The layout of the response is the following:
```json
{
	"ok": true,
	"data": {
		...
	}
}
```

### /range
This endpoint shows the data in the dataset filtered by the provided range of dates.
It looks for 2 query parameters of string type representing the start date and the end date.
The date parameters *must* be in the format *YYYY-MM-DD*.
- `start`: the starting date of the range
- `end`: the ending date of the range

### /kpi
This endpoint shows the KPI for each area and the number of products produced for each product code.
This endpoint accepts the following query parameters of integer type:
- `day` to filter the dataset by day
- `month` to filter the dataset by month
- `year` to filter the dataset by year

### /kpi/range
This endpoint shows the KPI for each area and the number of products produced for each product code in the given range of dates.
It looks for 2 query parameters of string type representing the start date and the end date.
The date parameters *must* be in the format *YYYY-MM-DD*.
- `start`: the starting date of the range
- `end`: the ending date of the range

### /kpi/year/{year}
This endpoint shows the average KPI for each area and the number of products produced for each product code in the given year.
The key difference from the KPI endpoint is that this KPI value is obtained from the average of monthly KPI values.
It expects an integer path parameter corresponding to the year.

### /kpi/year
This endpoint is the same as the one above except that it evaluates for the current year.

### /kpi/year/plot/{area}/{year}
This endpoint returns a bars plot as a PNG image that shows the average KPI for each month.
It expects two path parameters:
- `area` - a case insensitive string representing the destination market of the products
- `year` - an integer representing the year of interest

### /kpi/year/plot/{area}
This endpoint is the same as the one above excepts that it evaluates for the current year.

## Running
Run it with:
```bash
python kpi/main.py
```

Test it with:
```bash
python -m unittest tests/test.py
```
