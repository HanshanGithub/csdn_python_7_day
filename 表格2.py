import xlwings as xw

filename = "D:/AmStorage/My_File/SCDN_test/file/grade.xlsx"
app = xw.App(visible=False,add_book=False)
app.dispaly_alerts = False
app.screen_updating = False

wb = app.books.open(filename)

sht0 = wb.sheets[0]
sht1 = wb.sheets[1]

sht1.range('A1').value
sht1.range('A2:A4').value
sht1.range(1,2).value

info = sht1.used_range
nrows = info.last_cell.row
ncols = info.last_cell.column
# 加上 option 读取二维的数据
# allData = sht.range('a1:e24').options(ndim=2).value
# 和上面读取的内容一样
allData = sht1.range((1,1),(nrows,ncols)).options(ndim=2).value
for dt in allData:
    print(dt)

wb.close()



