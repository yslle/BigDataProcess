#!/usr/bin/python3
import openpyxl

wb = openpyxl.load_workbook("student.xlsx")
ws = wb['Sheet1']

row_id = 1;
for row in ws:
    if row_id != 1:
        sum_v = ws.cell(row = row_id, column = 3).value * 0.3
        sum_v += ws.cell(row = row_id, column = 4).value * 0.35
        sum_v += ws.cell(row = row_id, column = 5).value * 0.34
        sum_v += ws.cell(row = row_id, column = 6).value
        ws.cell(row = row_id, column = 7).value = sum_v
    row_id += 1

studentNum = row_id - 1
score = []

row_id = 1
for row in ws:
    if row_id != 1:
        total = ws.cell(row = row_id, column = 7).value
        score.append(total)
#scoreList = sorted(score)

print(score)
#print(scoreList)

wb.save("student.xlsx")
