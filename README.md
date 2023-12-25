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

### /kpi/range

### /kpi/year/{year}

### /kpi/year
