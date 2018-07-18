
import openpyxl

book = openpyxl.load_workbook("email_data.xlsx")
sheet = book.active

test = sheet['A2']
print(test.value)
