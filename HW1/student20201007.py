#!/usr/bin/python3

import openpyxl

wb = openpyxl.load_workbook("student.xlsx")
ws=wb.active #활성 시트 불러오기 

min_row=2
total_list=[]
grade_list=[]
for row in range(min_row,ws.max_row+1):
    midterm = ws.cell(column=3,row=row).value
    final = ws.cell(column=4,row=row).value
    homework = ws.cell(column=5,row=row).value
    attendance = ws.cell(column=6,row=row).value


    total = round(midterm * 0.3 + final * 0.35 + homework * 0.34 + attendance * 0.01,2)
    total_list.append([row,total])
    ws.cell(column=7,row=row,value=total)

#정렬
total_list2=sorted(total_list, key=lambda i:i[1],reverse=True) 
# print(total_list)
# print(total_list2)

#전체 학생 수
student=len(total_list2)

#3. A,B,C 비율 나누기, F학점
Fstu=0
for _, total in total_list:
    if total < 40.00:
        Fstu += 1

student2=student-Fstu
# Astu= int(student*0.3)
# Bstu= int(student*0.7)- Astu
# Cstu= student-(Astu+Bstu+Fstu)
Astu = int(student2 * 0.3)
Bstu = int(student2 * 0.4)
Cstu = int(student2 * 0.3)
#4.플러스 제로 비율 나누기 
Aplus=int(Astu*0.5)
Bplus=int(Bstu*0.5)
Cplus=int(Cstu*0.5)


#학점 부여
for i in range(Astu):
    ws.cell(row=total_list2[i][0], column=8).value = 'A0'
for i in range(Aplus):
    ws.cell(row=total_list2[i][0], column=8).value = 'A+'
for i in range(Astu,Astu+Bstu):
    ws.cell(row=total_list2[i][0], column=8).value = 'B0'
for i in range(Astu,Astu+Bplus):
    ws.cell(row=total_list2[i][0], column=8).value = 'B+'
for i in range(Astu+Bstu,Astu+Bstu+Cstu):
    ws.cell(row=total_list2[i][0], column=8).value = 'C0'
for i in range(Astu+Bstu,Astu+Bstu+Cplus):
    ws.cell(row=total_list2[i][0], column=8).value = 'C+'
    
for i in range(student2, student):
    ws.cell(row=total_list2[i][0], column=8).value = 'F'        
   
        
        
  

    
wb.save('student.xlsx')
wb.close()