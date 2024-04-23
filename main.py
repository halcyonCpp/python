'''题目6：
员工的计算机技能考核成绩保存在cj.csv文件文件中
读取文件，计算每个员工的平均成绩，及考核等级。考核等级评定如下：
等级分类 计算规则
不合格 5个考核科目中任一科目成绩低于60分
及格 60分≤ 平均成绩 <75分
良 75分≤ 平均成绩 <85分
优 平均成绩 ≥85分
将处理后的结果写入到cjresult.csv文件中。'''
import csv
# 读取原始数据
csv_file_path = 'C:\\Users\\DELL\\Desktop\\cj.csv'
data = []
with open(csv_file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # 处理数据
        a = row['Word']
        b = row['Outlook']
        c = row['Visio']
        d = row['Excel']
        e = row['PowerPoint']
        # 计算平均成绩
        score = (a + b + c + d + e) / 5
        row['平均成绩'] = score
        # 计算等级
        if a < 60 or b < 60 or c < 60 or d < 60 or e < 60:
            row['等级'] = '不及格'
        else:
            if score >= 85:
                row['等级'] = '优'
            elif score >= 75:
                row['等级'] = '良'
            elif score >= 60:
                row['等级'] = '及格'
        data.append(row)
# 写入处理后的数据到新文件
csv_file_result = 'C:\\Users\\DELL\\Desktop\\cjresult.csv'
with open(csv_file_result, 'w', newline='') as file:
    fieldnames = ['部门', '员工编号', '性别', '姓名', '年龄','Word', 'Outlook', 'Visio', 'Excel', 'PowerPoint', '平均成绩', '等级']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
    print('处理完成！')