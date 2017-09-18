#!python3

from stats import text_in_dir_stats
import xlsxwriter


dictionary = text_in_dir_stats()
workbook = xlsxwriter.Workbook('zipf.xlsx')
worksheet = workbook.add_worksheet()
row = 0
for [key, value] in dictionary:
	worksheet.write(row, 0, row)
	worksheet.write(row, 1, value)
	worksheet.write(row, 2, key)
	row += 1
workbook.close()