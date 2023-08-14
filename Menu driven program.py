#Menu Program For Storing data of employees

#After Running the program for 1st time Comment the 2 lines below
#Or you can create a text file named Data.txt and Delete the 2 lines
# a=open('Data.txt','w')
# a.close()
#^^^^^^^^^^^^^^^^^^^^^^^^^
def code():
    a=open('Data.txt','r')
    r=a.readlines()
    for i in r:
        c=i.split()
        l.append(c[0])
    if l==[]:
        return 1
    else:
        k=1+int(l[-1])
        return k


while True:
    c=[]
    w=[1,2,3,4,5]
    s=0
    nu=[]
    l=[]
    print('_____________Welcome_____________')
    print('Choose What you want to do :)')
    print('1.Add an employee')
    print('2.Print full employee list')
    print('3.Edit an employees Details')
    print('4.Delete an employee')
    print('5.Exit')
    ch=int(input('Enter your choice:--->'))
    print('===========================')
    if ch not in w:
        print('Wrong choice')
        continue
    
#Code to Add an Employee
    if ch==1:
        a=open('Data.txt','a')
        print('_____________')
        print('Entry number:--->',code())
        name=input('Enter Name:-->')
        age=input('Enter Age:-->')
        job=input('Enter Job:-->')
        country=input('Enter Nationality:-->')
        print('Entry No',code(),'Finished')
        print(' ')
        v=[str(code())+' ',name+' ',age+' ',job+' ',country+' ','\n']
        a.writelines(v)
        a.close()
        print('Data Saved  :)')

#code to Read full list    
    if ch==2:
        print('List shown as [No ID,Name,Age,Job,Nationality]')
        a=open('Data.txt','r')
        r=a.readlines()
        for i in r:
            c=i.split()
            l.append(c)
        for i in l:
            print(i)
        a.close()
        l=[]
        c=[]
        print('==============================')

#Code to edit an entry
    if ch==3:
        q=input('Enter the No ID of the person to edit:--->')
        a=open('Data.txt','r')
        r=a.readlines()
        for i in r:
            c=i.split()
            l.append(c)
        for i in l:
            if i[0]==q:
                print('You are Editing:-->',i)
                print('----------')
                print('1.Name')
                print('2.Age')
                print('3.Job')
                print('4.Nationality')
                t=int(input('Enter your choice to edit:---->'))
                if t==1:
                    name=input('Enter new Name:-->')
                    v=[q+' ',name+' ',i[2]+' ',i[3]+' ',i[4]+' ','\n']
                    nu.append(v)
                elif t==2:
                    age=input('Enter new Age:-->')
                    v=[q+' ',i[1]+' ',age+' ',i[3]+' ',i[4]+' ','\n']
                    nu.append(v)
                elif t==3:
                    job=input('Enter new Job:-->')
                    v=[q+' ',i[1]+' ',i[2]+' ',job+' ',i[4]+' ','\n']
                    nu.append(v)
                elif t==4:
                    country=input('Enter new Nationality:-->')
                    v=[q+' ',i[1]+' ',i[2]+' ',i[3]+' ',country+' ','\n']
                    nu.append(v)
            if  i[0]!=q:
                i[0]=i[0]+' '
                i[1]=i[1]+' '
                i[2]=i[2]+' '
                i[3]=i[3]+' '
                i[4]=i[4]+' '
                i.append('\n')
                nu.append(i)
        a.close()
        a=open('Data.txt','w')
        for i in nu:
            a.writelines(i)
        a.close()
        print('Data Saved  :)')
    l=[]

#code to delete an entry
    if ch==4:
        q=input('Enter the No ID of the person to Delete:--->')
        a=open('Data.txt','r')
        r=a.readlines()
        for i in r:
            c=i.split()
            l.append(c)
        for i in l:
            if i[0]==q:
                wert=0
            if  i[0]!=q:
                i[0]=i[0]+' '
                i[1]=i[1]+' '
                i[2]=i[2]+' '
                i[3]=i[3]+' '
                i[4]=i[4]+' '
                i.append('\n')
                nu.append(i)
        a.close()
        a=open('Data.txt','w')
        for i in nu:
            a.writelines(i)
        a.close()
        print('Data Saved  :)')
            
#code to exit
    if ch==5:
        break
                a.writelines(' '.join(i) + '\n')
        print('Data Saved  :)')
    
    if ch == 5:
        break
