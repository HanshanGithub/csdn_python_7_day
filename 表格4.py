import random
import xlwt
import xlrd
import os

# 存放excel表格的目录，EXCEL文件夹要存在
dir_path = "./EXCEL"
# 文件类型
file_type = 'xls'

# 随机生成名字
def generate_name():
    first_name = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
    last_name = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
    first_name = random.choice(first_name)
    last_name = "".join(random.choice(last_name) for i in range(2))
    return first_name + last_name

# 测试名字效果
# print(generate_name())

# 随机生成成绩
def generate_grade():
    return random.randint(60, 100)
# 创建成绩表
def generate_grade_excel(course, name_list):
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('sheet1')
    sheet.write(0, 0, '姓名')
    sheet.write(0, 1, '期中成绩')
    sheet.write(0, 2, '期末成绩')
    sheet.write(0, 3, '平时成绩')
    sheet.write(0, 4, '学科得分')
    sheet.write(0, 5, '学号') # nit
    for index in range(1, len(name_list)+1):
        mid = generate_grade()
        fin = generate_grade()
        usual = generate_grade()
        subj = int((mid + fin) * 0.35 + usual * 0.3)
        number = "20210926" + str(100+index) # 添加学号
        sheet.write(index, 0, name_list[index - 1])
        sheet.write(index, 1, mid)
        sheet.write(index, 2, fin)
        sheet.write(index, 3, usual)
        sheet.write(index, 4, subj)
        sheet.write(index, 5, number)
    wb.save(dir_path + '/' + course + '.xls')
    #wb.save(course + '.xls')
    
# 生成四份相同格式 不同科目成绩的表格
def create_tables():
    # 嵌套for循环
    namelist = [generate_name() for i in range(50)]
    for i in ['大学物理', '高等数学', '大学英语', 'Python程序设计']:
        generate_grade_excel(i, namelist)

# 创建四种科目成绩
create_tables()

# # 遍历文件夹下的所有xls表格文件
# def get_all_excel(walk_path):
#     file_list = []
#     for root_dir, sub_dir, files in os.walk(r'' + walk_path):
#         for file in files:
#             if file.endswith(file_type):
#                 file_name = os.path.join(root_dir, file)
#                 file_list.append(file_name)
#     return file_list

# # 汇总成绩
# def summary():
#     file_list = get_all_excel(dir_path)
#     stu = {}
#     cursor = [os.path.basename(file).replace('.xls', '') for file in file_list]
#     for file in file_list:
#         wb = xlrd.open_workbook(file)
#         sheet = wb.sheet_by_index(0)
#         for index in range(1, sheet.nrows):
#             stu.setdefault(sheet.cell(index, 0).value, []).append(sheet.cell(index, 4).value)
#     wb = xlwt.Workbook()
#     sheet = wb.add_sheet('总成绩')
#     sheet.write(0, 0, '姓名')
#     sheet.write(0, 1, cursor[0])
#     sheet.write(0, 2, cursor[1])
#     sheet.write(0, 3, cursor[2])
#     sheet.write(0, 4, cursor[3])
#     index = 1
#     for name, grades in stu.items():
#         sheet.write(index, 0, name)
#         sheet.write(index, 1, grades[0])
#         sheet.write(index, 2, grades[1])
#         sheet.write(index, 3, grades[2])
#         sheet.write(index, 4, grades[3])
#         index = index + 1
#     wb.save('汇总成绩.xls')

# summary()
