#!/usr/bin/env python3

import unittest
from kpi.pool import Pool, Product
from datetime import datetime


products = Pool([
	Product("test", "test_area_1", "2023-01-01 00:00:00.000", "1"),

	Product("test", "test_area_1", "2023-02-01 00:00:00.000", "1"),
	Product("test", "test_area_1", "2023-02-01 00:00:00.000", "2"),

	Product("test", "test_area_1", "2023-03-01 00:00:00.000", "1"),
	Product("test", "test_area_1", "2023-03-01 00:00:00.000", "2"),
	Product("test", "test_area_1", "2023-03-01 00:00:00.000", "3"),

	Product("test", "test_area_1", "2023-04-01 00:00:00.000", "1"),
	Product("test", "test_area_1", "2023-04-01 00:00:00.000", "2"),
	Product("test", "test_area_1", "2023-04-01 00:00:00.000", "3"),
	Product("test", "test_area_1", "2023-04-01 00:00:00.000", "4"),

	Product("test", "test_area_1", "2023-05-01 00:00:00.000", "1"),
	Product("test", "test_area_1", "2023-05-01 00:00:00.000", "2"),
	Product("test", "test_area_1", "2023-05-01 00:00:00.000", "3"),
	Product("test", "test_area_1", "2023-05-01 00:00:00.000", "4"),
	Product("test", "test_area_1", "2023-05-01 00:00:00.000", "5"),

	Product("test", "test_area_1", "2023-06-01 00:00:00.000", "1"),
	Product("test", "test_area_1", "2023-06-01 00:00:00.000", "2"),
	Product("test", "test_area_1", "2023-06-01 00:00:00.000", "3"),
	Product("test", "test_area_1", "2023-06-01 00:00:00.000", "4"),
	Product("test", "test_area_1", "2023-06-01 00:00:00.000", "5"),
	Product("test", "test_area_1", "2023-06-01 00:00:00.000", "6"),

	Product("test", "test_area_1", "2023-07-01 00:00:00.000", "1"),
	Product("test", "test_area_1", "2023-07-01 00:00:00.000", "2"),
	Product("test", "test_area_1", "2023-07-01 00:00:00.000", "3"),
	Product("test", "test_area_1", "2023-07-01 00:00:00.000", "4"),
	Product("test", "test_area_1", "2023-07-01 00:00:00.000", "5"),
	Product("test", "test_area_1", "2023-07-01 00:00:00.000", "6"),
	Product("test", "test_area_1", "2023-07-01 00:00:00.000", "7"),

	Product("test", "test_area_1", "2023-08-01 00:00:00.000", "1"),
	Product("test", "test_area_1", "2023-08-01 00:00:00.000", "2"),
	Product("test", "test_area_1", "2023-08-01 00:00:00.000", "3"),
	Product("test", "test_area_1", "2023-08-01 00:00:00.000", "4"),
	Product("test", "test_area_1", "2023-08-01 00:00:00.000", "5"),
	Product("test", "test_area_1", "2023-08-01 00:00:00.000", "6"),
	Product("test", "test_area_1", "2023-08-01 00:00:00.000", "7"),
	Product("test", "test_area_1", "2023-08-01 00:00:00.000", "8"),

	Product("test", "test_area_1", "2023-09-01 00:00:00.000", "1"),
	Product("test", "test_area_1", "2023-09-01 00:00:00.000", "2"),
	Product("test", "test_area_1", "2023-09-01 00:00:00.000", "3"),
	Product("test", "test_area_1", "2023-09-01 00:00:00.000", "4"),
	Product("test", "test_area_1", "2023-09-01 00:00:00.000", "5"),
	Product("test", "test_area_1", "2023-09-01 00:00:00.000", "6"),
	Product("test", "test_area_1", "2023-09-01 00:00:00.000", "7"),
	Product("test", "test_area_1", "2023-09-01 00:00:00.000", "8"),
	Product("test", "test_area_1", "2023-09-01 00:00:00.000", "9"),

	Product("test", "test_area_1", "2023-10-01 00:00:00.000", "1"),
	Product("test", "test_area_1", "2023-10-01 00:00:00.000", "2"),
	Product("test", "test_area_1", "2023-10-01 00:00:00.000", "3"),
	Product("test", "test_area_1", "2023-10-01 00:00:00.000", "4"),
	Product("test", "test_area_1", "2023-10-01 00:00:00.000", "5"),
	Product("test", "test_area_1", "2023-10-01 00:00:00.000", "6"),
	Product("test", "test_area_1", "2023-10-01 00:00:00.000", "7"),
	Product("test", "test_area_1", "2023-10-01 00:00:00.000", "8"),
	Product("test", "test_area_1", "2023-10-01 00:00:00.000", "9"),
	Product("test", "test_area_1", "2023-10-01 00:00:00.000", "10"),

	Product("test", "test_area_1", "2023-11-01 00:00:00.000", "1"),
	Product("test", "test_area_1", "2023-11-01 00:00:00.000", "2"),
	Product("test", "test_area_1", "2023-11-01 00:00:00.000", "3"),
	Product("test", "test_area_1", "2023-11-01 00:00:00.000", "4"),
	Product("test", "test_area_1", "2023-11-01 00:00:00.000", "5"),
	Product("test", "test_area_1", "2023-11-01 00:00:00.000", "6"),
	Product("test", "test_area_1", "2023-11-01 00:00:00.000", "7"),
	Product("test", "test_area_1", "2023-11-01 00:00:00.000", "8"),
	Product("test", "test_area_1", "2023-11-01 00:00:00.000", "9"),
	Product("test", "test_area_1", "2023-11-01 00:00:00.000", "10"),
	Product("test", "test_area_1", "2023-11-01 00:00:00.000", "11"),

	Product("test", "test_area_1", "2023-12-01 00:00:00.000", "1"),
	Product("test", "test_area_1", "2023-12-01 00:00:00.000", "2"),
	Product("test", "test_area_1", "2023-12-01 00:00:00.000", "3"),
	Product("test", "test_area_1", "2023-12-01 00:00:00.000", "4"),
	Product("test", "test_area_1", "2023-12-01 00:00:00.000", "5"),
	Product("test", "test_area_1", "2023-12-01 00:00:00.000", "6"),
	Product("test", "test_area_1", "2023-12-01 00:00:00.000", "7"),
	Product("test", "test_area_1", "2023-12-01 00:00:00.000", "8"),
	Product("test", "test_area_1", "2023-12-01 00:00:00.000", "9"),
	Product("test", "test_area_1", "2023-12-01 00:00:00.000", "10"),
	Product("test", "test_area_1", "2023-12-01 00:00:00.000", "11"),
	Product("test", "test_area_1", "2023-12-01 00:00:00.000", "12")
])


class KPITest(unittest.TestCase):
	def test_kpi(self):
		kpi = products.kpi()
		self.assertEqual(kpi["test_area_1"]["kpi"], 12)

	def test_year_kpi(self):
		kpi = products.year_avg_kpi()
		self.assertEqual(kpi["test_area_1"]["kpi"], (78 / 12))

	def test_filters(self):
		self.assertEqual(products.month(9).day(1).kpi()["test_area_1"]["kpi"], 9)
		self.assertEqual(products.month(3).kpi()["test_area_1"]["kpi"], 3)
		self.assertEqual(products.range(datetime(2023, 1, 1), datetime(2023, 3, 1)).kpi()["test_area_1"]["kpi"], 3)
