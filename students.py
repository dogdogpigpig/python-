def main():
    dict_2000={'ID': 2000, 'name': 'Mike', 'math': 96, 'Chinese': 66, 'English': 74}
    dict_2001={'ID': 2001, 'name': 'John', 'math': 94, 'Chinese': 88, 'English': 62}
    student_list=[dict_2000, dict_2001]
    while True:
        #for i in student_list:
            #print(i)
        menu()
        choice=int(input('please make a choice:'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('Sure? yes or no:')
                if answer=='yes':
                    print('Thanks!!!')
                    break
                else:
                    continue
            elif choice==1:
                add(student_list)
            elif choice==2:
                delete(student_list)
            elif choice==3:
                change(student_list)
            elif choice==4:
                sort(student_list)
            elif choice==5:
                search(student_list)
            elif choice==6:
                totle(student_list)
            elif choice==7:
                show(student_list)
        else:
            print('input error!please input again:')
            continue
def menu():
    print('-'*7,' student information','-'*7)
    print('              1.add')
    print('              2.delete')
    print('              3.change')
    print('              4.sort')
    print('              5.search')
    print('              6.totle')
    print('              7.show')
    print('              0.turn off')
    print('-'*34)
def add(student_list):
    while True:
        ID=int(input('please input ID number:'))
        if not ID:
            break
        name=input('please input name:')
        try:
            math = int(input('please input math grade:'))
            Chinese = int(input('please input Chinese grade:'))
            English = int(input('please input English name:'))
        except:
            print('input error!please input again')
            continue
        student = {'ID': ID, 'name': name, 'math': math, 'Chinese': Chinese, 'English': English}
        student_list.append(student)
        answer=input('add again? yes or no:')
        if answer=='yes':
            continue
        else:
            break
def delete(student_list):
   while True:
       student_ID=int(input('please input ID number:'))
       will_delete=[]
       for student in student_list:
           if student_ID==student['ID']:
               will_delete.append(student)
       if len(will_delete)>0:
           for student in will_delete:
               student_list.remove(student)
           print('delete successfully')
       else:
           print('Not Found')
       answer=input('delete again? yes or no:')
       if answer=='yes':
           continue
       else:
           break
def change(student_list):
    while True:
        ID=int(input('please input ID number:'))
        found=False
        for student in student_list:
            if ID==student['ID']:
                found=True
                break;
        if found:
            name=input('please input changed name:')
            try:
                math=int(input('please input changed math grade:'))
                Chinese=int(input('please input changed Chinese grade:'))
                English=int(input('please input changed English name:'))
            except:
                print('input error!please input again')
                continue
            student['name']=name
            student['math']=math
            student['Chinese']=Chinese
            student['English']=English
        else:
            print('Not Found')
        answer=input('change again? yes or no:')
        if answer=='yes':
            continue
        else:
            break
def sort(student_list):
    subject=input('please make a choice:\nA.math\t\t\tB.Chinese\t\t\tC.English\t\t\tD.the sum\n')
    student_dict={'ID':0,'name':a,'math':0,'Chinese':0,'English':0}
    if subject=='A':
        for i in range(len(student_list)-1):
            for j in range(len(student_list)-i-1):
                if student_list[j]['math']<student_list[j+1]['math']:
                    student_list[j],student_list[j+1]=student_list[j+1],student_list[j]
                    #student_dict=student_list[j]
                    #student_list[j]=student_list[j+1]
                    #student_list[j+1]=student_dict
    elif subject=='B':
        for i in range(len(student_list)-1):
            for j in range(len(student_list)-i-1):
                if student_list[j]['Chinese']<student_list[j+1]['Chinese']:
                    student_list[j],student_list[j+1]=student_list[j+1],student_list[j]
    elif subject=='C':
        for i in range(len(student_list)-1):
            for j in range(len(student_list)-i-1):
                if student_list[j]['English']<student_list[j+1]['English']:
                    student_list[j],student_list[j+1]=student_list[j+1],student_list[j]
    elif subject=='D':
        #student_list=sorted(student_list,key=lambda x:x['math']+x['Chinese']+x['English'],reverse=True)
        for i in range(len(student_list)-1):
            for j in range(len(student_list)-1-i):
                if student_list[j]['math']+student_list[j]['Chinese']+student_list[j]['English']<student_list[j+1]['math']+student_list[j+1]['Chinese']+student_list[j+1]['English']:
                    student_list[j],student_list[j+1] = student_list[j+1],student_list[j]
    else:
        print('input error!')
    for i in student_list:
        print(i)
def search(student_list):
    while True:
        ID = int(input('please input the ID number:'))
        found=False
        for student in student_list:
            if ID == student['ID']:
                found=True
                break
        if found:
            print('Have Founded')
            print(student)
        else:
            print('Not Found!')
        answer=input('search again? yes or no:')
        if answer=='yes':
            continue
        else:
            break
def totle(student_list):
    print('学生总数为:',len(student_list))
def show(student_list):
    for i in student_list:
        print(i)
if __name__ == '__main__':
    main()