import xlsxwriter

OutWorkbook = xlsxwriter.Workbook("Book9.xlsx")
OutSheet = OutWorkbook.add_worksheet()

Names = ['Kile', 'michele', 'Andrew']
Values = [1, 2, 3]
OutSheet.write('A1', 'Names')

OutWorkbook.close()