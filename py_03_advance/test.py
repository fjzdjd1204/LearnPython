import xlrd

book = xlrd.open_workbook("NIB-OVHC application.xlsx")
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
for rx in range(sh.nrows):
    print(sh.row(rx))