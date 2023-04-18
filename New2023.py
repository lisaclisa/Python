
grade = 'nothing'


classsize = 5
StudentName = ['Mark','Lisa','John','Lily','Lucy']
StudentMark = [[55,79,43,20],[34,32,46,55],[78,76,98,87],[89,90,76,56],[43,89,32,65]]
SubjectNo = 4

total = 0
fail = 0
des = 0
passscore =0
merit = 0
for i in range(classsize):
    total = 0
    for m in StudentMark[i]:
        
        total = total + m
    average = int(total/SubjectNo)
    if average >= 70:
        grade = 'destinction'
        des = des + 1
    elif average < 70 and average >= 55:
            grade = 'merit'
            merit = merit + 1
    elif average <55 and average >= 40:
            grade = 'pass'
            passscore = passscore + 1
    else:
            grade = 'fail'
            fail = fail + 1
    print(StudentName[i],'total',total,'average', average,grade)

print('total destinction:',des,'total merit:',merit,'total pass:',passscore,'total fail',fail)
