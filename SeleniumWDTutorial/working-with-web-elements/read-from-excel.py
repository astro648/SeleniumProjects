import xlrd

workbook = xlrd.open_workbook("Book1.xls")
sheet = workbook.sheet_by_name("Sheet1")

# Get number of rows with data in excel sheet
rowcount = sheet.nrows
# Get number of columns with data in each row. Returns highest number
colcount = sheet.ncols
print(rowcount)
print(colcount)

result_data =[]
for curr_row in range(1, rowcount, 1):
    row_data = []

    for curr_col in range(1, colcount-1, 1):
        # Read the data in the current cell
        data = sheet.cell_value(curr_row, curr_col)
        print(data)
        row_data.append(data)

    result_data.append(row_data)