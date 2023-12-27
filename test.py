#!/usr/bin/env python3

import main
from datetime import datetime

products = main.Pool([
	main.Product("test", "test_area_1", "2023-01-01 00:00:00.000", "1"),

	main.Product("test", "test_area_1", "2023-02-01 00:00:00.000", "1"),
	main.Product("test", "test_area_1", "2023-02-01 00:00:00.000", "2"),

	main.Product("test", "test_area_1", "2023-03-01 00:00:00.000", "1"),
	main.Product("test", "test_area_1", "2023-03-01 00:00:00.000", "2"),
	main.Product("test", "test_area_1", "2023-03-01 00:00:00.000", "3"),

	main.Product("test", "test_area_1", "2023-04-01 00:00:00.000", "1"),
	main.Product("test", "test_area_1", "2023-04-01 00:00:00.000", "2"),
	main.Product("test", "test_area_1", "2023-04-01 00:00:00.000", "3"),
	main.Product("test", "test_area_1", "2023-04-01 00:00:00.000", "4"),

	main.Product("test", "test_area_1", "2023-05-01 00:00:00.000", "1"),
	main.Product("test", "test_area_1", "2023-05-01 00:00:00.000", "2"),
	main.Product("test", "test_area_1", "2023-05-01 00:00:00.000", "3"),
	main.Product("test", "test_area_1", "2023-05-01 00:00:00.000", "4"),
	main.Product("test", "test_area_1", "2023-05-01 00:00:00.000", "5"),

	main.Product("test", "test_area_1", "2023-06-01 00:00:00.000", "1"),
	main.Product("test", "test_area_1", "2023-06-01 00:00:00.000", "2"),
	main.Product("test", "test_area_1", "2023-06-01 00:00:00.000", "3"),
	main.Product("test", "test_area_1", "2023-06-01 00:00:00.000", "4"),
	main.Product("test", "test_area_1", "2023-06-01 00:00:00.000", "5"),
	main.Product("test", "test_area_1", "2023-06-01 00:00:00.000", "6"),

	main.Product("test", "test_area_1", "2023-07-01 00:00:00.000", "1"),
	main.Product("test", "test_area_1", "2023-07-01 00:00:00.000", "2"),
	main.Product("test", "test_area_1", "2023-07-01 00:00:00.000", "3"),
	main.Product("test", "test_area_1", "2023-07-01 00:00:00.000", "4"),
	main.Product("test", "test_area_1", "2023-07-01 00:00:00.000", "5"),
	main.Product("test", "test_area_1", "2023-07-01 00:00:00.000", "6"),
	main.Product("test", "test_area_1", "2023-07-01 00:00:00.000", "7"),

	main.Product("test", "test_area_1", "2023-08-01 00:00:00.000", "1"),
	main.Product("test", "test_area_1", "2023-08-01 00:00:00.000", "2"),
	main.Product("test", "test_area_1", "2023-08-01 00:00:00.000", "3"),
	main.Product("test", "test_area_1", "2023-08-01 00:00:00.000", "4"),
	main.Product("test", "test_area_1", "2023-08-01 00:00:00.000", "5"),
	main.Product("test", "test_area_1", "2023-08-01 00:00:00.000", "6"),
	main.Product("test", "test_area_1", "2023-08-01 00:00:00.000", "7"),
	main.Product("test", "test_area_1", "2023-08-01 00:00:00.000", "8"),

	main.Product("test", "test_area_1", "2023-09-01 00:00:00.000", "1"),
	main.Product("test", "test_area_1", "2023-09-01 00:00:00.000", "2"),
	main.Product("test", "test_area_1", "2023-09-01 00:00:00.000", "3"),
	main.Product("test", "test_area_1", "2023-09-01 00:00:00.000", "4"),
	main.Product("test", "test_area_1", "2023-09-01 00:00:00.000", "5"),
	main.Product("test", "test_area_1", "2023-09-01 00:00:00.000", "6"),
	main.Product("test", "test_area_1", "2023-09-01 00:00:00.000", "7"),
	main.Product("test", "test_area_1", "2023-09-01 00:00:00.000", "8"),
	main.Product("test", "test_area_1", "2023-09-01 00:00:00.000", "9"),

	main.Product("test", "test_area_1", "2023-10-01 00:00:00.000", "1"),
	main.Product("test", "test_area_1", "2023-10-01 00:00:00.000", "2"),
	main.Product("test", "test_area_1", "2023-10-01 00:00:00.000", "3"),
	main.Product("test", "test_area_1", "2023-10-01 00:00:00.000", "4"),
	main.Product("test", "test_area_1", "2023-10-01 00:00:00.000", "5"),
	main.Product("test", "test_area_1", "2023-10-01 00:00:00.000", "6"),
	main.Product("test", "test_area_1", "2023-10-01 00:00:00.000", "7"),
	main.Product("test", "test_area_1", "2023-10-01 00:00:00.000", "8"),
	main.Product("test", "test_area_1", "2023-10-01 00:00:00.000", "9"),
	main.Product("test", "test_area_1", "2023-10-01 00:00:00.000", "10"),

	main.Product("test", "test_area_1", "2023-11-01 00:00:00.000", "1"),
	main.Product("test", "test_area_1", "2023-11-01 00:00:00.000", "2"),
	main.Product("test", "test_area_1", "2023-11-01 00:00:00.000", "3"),
	main.Product("test", "test_area_1", "2023-11-01 00:00:00.000", "4"),
	main.Product("test", "test_area_1", "2023-11-01 00:00:00.000", "5"),
	main.Product("test", "test_area_1", "2023-11-01 00:00:00.000", "6"),
	main.Product("test", "test_area_1", "2023-11-01 00:00:00.000", "7"),
	main.Product("test", "test_area_1", "2023-11-01 00:00:00.000", "8"),
	main.Product("test", "test_area_1", "2023-11-01 00:00:00.000", "9"),
	main.Product("test", "test_area_1", "2023-11-01 00:00:00.000", "10"),
	main.Product("test", "test_area_1", "2023-11-01 00:00:00.000", "11"),

	main.Product("test", "test_area_1", "2023-12-01 00:00:00.000", "1"),
	main.Product("test", "test_area_1", "2023-12-01 00:00:00.000", "2"),
	main.Product("test", "test_area_1", "2023-12-01 00:00:00.000", "3"),
	main.Product("test", "test_area_1", "2023-12-01 00:00:00.000", "4"),
	main.Product("test", "test_area_1", "2023-12-01 00:00:00.000", "5"),
	main.Product("test", "test_area_1", "2023-12-01 00:00:00.000", "6"),
	main.Product("test", "test_area_1", "2023-12-01 00:00:00.000", "7"),
	main.Product("test", "test_area_1", "2023-12-01 00:00:00.000", "8"),
	main.Product("test", "test_area_1", "2023-12-01 00:00:00.000", "9"),
	main.Product("test", "test_area_1", "2023-12-01 00:00:00.000", "10"),
	main.Product("test", "test_area_1", "2023-12-01 00:00:00.000", "11"),
	main.Product("test", "test_area_1", "2023-12-01 00:00:00.000", "12")
])

def test_kpi():
	kpi = products.kpi()
	assert kpi["test_area_1"]["kpi"] == 12

def test_year_kpi():
	kpi = products.year_avg_kpi()
	assert kpi["test_area_1"]["kpi"] == (78 / 12)

def test_filters():
	assert products.month(9).day(1).kpi()["test_area_1"]["kpi"] == 9
	assert products.month(3).kpi()["test_area_1"]["kpi"] == 3
	assert products.range(datetime(2023, 1, 1), datetime(2023, 3, 1)).kpi()["test_area_1"]["kpi"] == 3


if __name__ == "__main__":
	test_kpi()
	test_year_kpi()
	test_filters()
