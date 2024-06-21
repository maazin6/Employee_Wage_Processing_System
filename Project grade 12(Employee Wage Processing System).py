print("EMPLOYEE WAGE PROCESSING SYSTEM")
print()
print('*'*50)
print()
#login function 

def login():
    print()
    print("Sample values for login(For teachers refernce):")
    print("Empid=1,password=pass,role=Admin")
    print("Empid=2,password=pass,role=Manager")
    print("Empid=3,password=pass,role=User")
    print("please ensure that these values are entered into the database via SQl")
    print()
    import mysql.connector
    mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="root",
         database="employee")

    
    loop=0
    while loop==0:
        login=[]
        print()
        print("1.Login")
        print()
        print("2.Exit")
        print()
        
        ch=int(input("enter Choice(1/2):"))
        print()
        print('*'*50)
        print()
        
        if ch==2:
            loop=1
            login=[0]
            break
        
        elif ch==1:
            loop1=0
            while loop1==0:
                id=int(input("Enter Employee Number:"))
                print()
                p=input("Enter Password:")
                print()
        
                x=mydb.cursor()

                x.execute("select Empid,password,Role,status from empdata where Empid=%d"%id)
                rec=x.fetchall()

                if len(rec)==0:
                    print("Employee Data Not Found!")
                    print()
                    print('*'*50)
                    break
                
                for i in rec:
                    
                    if i[0]==id and i[1]==p:

                        if i[3]=='t' or i[3]=='T':
                            print("This user has been Terminated")
                            print('*'*50)
                            print()
                            loop1=1
                            login=[0]
                            break

                        else:

                            print("Correct Password!")
                            print()
                            print('*'*50)
                            print()
                            loop1=1
                            loop=1
                            login=i
                            print()
                        
                    
                    else:
                        print("Incorrect Password!Try Again")
                        print()
                        loop1=1
                
        
    print()
    return login
    #login=[Empid,password,role,status]

#user function

def user(id):
    
    loopu=0
    while loopu==0:
        
        print("1.View Personal Data")
        print()
        print("2.View Salary Data")
        print()
        print("3.Change Personal Password")
        print()
        print("4.Exit")
        print()
        
        chu=int(input("Enter Choice(1/2/3/4):"))
        print()
        print('*'*50)
        print()
        
        if chu==1:
            
            specific_empdata(id)

        elif chu==2:
            
            specific_salary(id)

        elif chu==4:
            loopu=1
            run()

        elif chu==3:
            password(id)

#manager function
            
def manager(id):
    
    loopm=0
    while loopm==0:
        
        print("1.View ")
        print()
    
        print("2.Display")
        print()
        
        print("3.Add ")
        print()
        
        print("4.Terminate Employee")
        print()

        print("5.Change Personal Password  ")
        print()
        
        print("6.Exit")
        print()

        chm=int(input("Enter Choice(1/2/3.../6):"))
        print()
        print('*'*50)
        print()
        
        if chm==1:
            view()

        elif chm==2:
            display()

        elif chm==3:
            add()

        elif chm==4:
            terminate()

        elif chm==6:
            loopm=1
            run()
            break

        elif chm==5:
            password(id)

#admin function
                
def admin(id):

    loopa=0
    while loopa==0:
        
        print("1.View")
        print()
        
        print("2.Display")
        print()
        
        print("3.Add")
        print()
        
        print("4.Update ")
        print()
        
        print("5.Terminate Employee")
        print()
        
        print("6.Delete")
        print()

        print("7.Change Personal Password")
        print()
        
        print("8.Exit")
        print()

        cha=int(input("Enter Choice(1/2/3.../8):"))
        print()
        print('*'*50)
        print()
        
        if cha==1:
            view()

        elif cha==2:
            display()

        elif cha==3:
            add()
            
        elif cha==4:
            update()
        
        elif cha==5:
            terminate()

        elif cha==6:
            delete()

        elif cha==8:
            loopa=1
            run()
            break

        elif cha==7:

            password(id)
        

#employee data function

def empdata():

    import mysql.connector
    mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="root",
         database="employee")
    
    x=mydb.cursor()
    x.execute("select * from empdata")
    rec=x.fetchall()
    
    for i in rec:
        print(i)
        print()
    print('*'*50)
    print()

#specific employee data
        
def specific_empdata(id):
    
    import mysql.connector
    mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="root",
         database="employee")

    count=0
    x=mydb.cursor()
    x.execute("select * from empdata where Empid=%d"%id)
    rec=x.fetchall()
    
    for i in rec:
        count+=1
        print(i)
        print()
        
    if count==0:
        print("No data found!")
        print()
    print('*'*50)
    print()

    return count


#salary data function

def salary():

    import mysql.connector
    mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="root",
         database="employee")
    
    x=mydb.cursor()
    x.execute("select * from salary")
    rec=x.fetchall()

    count=0
    for i in rec:
        count+=1
        print(i)
        print()

    if count==0:
        print("No data found!")
        print()
    print('*'*50)
    print()
    
        
#specific salary data
        
def specific_salary(id):
    
    import mysql.connector
    mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="root",
         database="employee")

    count=0
    x=mydb.cursor()
    x.execute("select * from salary where Empid=%d"%id)
    rec=x.fetchall()
    
    for i in rec:
        count+=1
        print(i)
        print()
        
    if count==0:
        print("No data found!")
        print()
        out=0
    print('*'*50)
    print()
    return count

#diplay data
        
def display():

    loop=0
    while loop==0:

        import mysql.connector
        mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="root",
         database="employee")
  
        print("1.Display all data")
        print()
        print("2.Display Active/Available Eployee Data")
        print()
        print("3.Display Terminated Eployee Data")
        print()
        print("4.Exit")
        print()
        
        ch=int(input("Enter Choice(1/2/3/4):"))
        print()

        if ch==1:

            count=0
            x=mydb.cursor()
            x.execute("select * from empdata natural join salary")
            rec=x.fetchall()
            
            for i in rec:
                count+=1
                print(i)
                print()
                
            if count==0:
                print("No data found!")
                print()

            print('*'*50)
            print()

        elif ch==2:

            count=0
            x=mydb.cursor()
            x.execute("select * from empdata natural join salary where empdata.status='a'")
            rec=x.fetchall()
            
            for i in rec:
                count+=1
                print(i)
                print()
                
            if count==0:
                print("No data found!")
                print()

            print('*'*50)
            print()

        elif ch==3:

            count=0
            x=mydb.cursor()
            x.execute("select * from empdata natural join salary where empdata.status='t'")
            rec=x.fetchall()
            
            for i in rec:
                count+=1
                print(i)
                print()
                
            if count==0:
                print("No data found!")
                print()

            print('*'*50)
            print()
                
        elif ch==4:
            loop=1
            print('*'*50)
            print()
            break
        
        loopc=0
        while loopc==0:
                    
            cont=input("Do You wish to Continue(yes/no):")
            print()
            print('*'*50)
            print()
            if cont.lower()=='yes':
                loopc=1

            elif cont.lower()=='no':
                loop=1
                loopc=1


#add employee data function
            
def addemp():

    import mysql.connector
    mydb = mysql.connector.connect(
             host="localhost",
             user="root",
             password="root",
             database="employee")
    
    print("Enter the following data:-")
    print()
    
    empid=int(input("Employee Number:"))
    print()

    count=0
    x=mydb.cursor()
    x.execute("select * from empdata where Empid=%d"%empid)
    rec=x.fetchall()
            
    for i in rec:
        count+=1
        
    if count==1:
        print("User already exists with Empid:",empid,"!")
        print()
        print('*'*50)
        print()
       
    elif count==0:
        
        empname=input("Employee Name:")
        print()
    
        designation=input("Designation:")
        print()

        r=['U','A','M']
        role=input("Role(Admin-'A'/Manager-'M'/User-'U'):")
        role=role.upper()
        print()
        while role not in r:
            print("Role only takes a value as:",r)
            print()
            role=input("Role(Admin-'A'/Manager-'M'/User-'U')):")
            print()

        s=['A','T']
        status=input("Status(Active-'A'/Terminated-'T'):")
        status=status.upper()
        while status not in s:
            print("Status only takes value as:",s)
            print()
            status=input("Status(Active-'A'/Terminated-'T'):")
            print()
        
        basic=float(input("Basic Salary:"))
        print()
        
        allowence=float(input("Monthly Allowence:"))
        print()
        
        x=mydb.cursor()

        sql=("INSERT into empdata(Empid,Empname,Designation,Role,status,basic, allowence) values(%s,%s,%s,%s,%s,%s,%s);")
        val=[empid,empname,designation,role,status,basic,allowence]
        x.execute(sql,val)
        
        try:
            mydb.commit()
            print("Data has been added!")
            print('*'*50)
            print()
            
        except:
            mydb.rollback()
            
        x.close()
        mydb.close()

# add salary data function

def addsal():
    import mysql.connector
    mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="root",
         database="employee")

    id=int(input("Enter Empid:"))
    print()
    count=0
    x=mydb.cursor()
    x.execute("select basic,allowence,status from empdata where Empid=%d"%id)
    rec=x.fetchall()
    
    for i in rec:
        count+=1
        data=i
        
    if count==0:
        print("Empid not found!")
        print()
        
    else:
        
        if data[2]=='t' or data[2]=='T':
                print("This Employee has been Terminated")
                print('*'*50)
                print()

        else:
        
            basic=data[0]
            allowence=data[1]
            
            basic_rate=(basic+allowence)/240            #basic rate
            overtime_rate=basic/240                     #over time rate

            m=['january','february','march','april','may','june','july','august','september','october','november','december']    
            month=input("Enter Month:")
            print()
            while month not in m:
                print("Enter an appropriate month!")
                month=input("Enter Month:")
                print()
                
            year=int(input("Enter Year:"))
            print()

            hours=float(input("Enter Basic Hours Worked:"))     #Normal Hours
            print()
            
            while hours>240 or hours<0:
                print("Invalid Input!basic hours cannot be over 240 hours or less than 0")
                print()
                hours=float(input("Enter Basic Hours Worked:"))
                print()

            basic_pay=hours*basic_rate

            normal_overtime=int(input("Enter Normal Overtime Hours:"))          #Normal Overtime
            print()
            
            while normal_overtime>72 or normal_overtime<0:
                print("Invalid Input!basic overtime hours cannot be over 72 hours or less than 0") #check value of normal overtime hours
                print()
                normal_overtime=int(input("Enter Normal Overtime Hours:"))
                print()

            normal_overtime_pay=normal_overtime*1.25*overtime_rate

            friday_overtime=int(input("Enter friday Overtime Hours:"))          #Friday Overtime
            print()
            
            while friday_overtime>20 or friday_overtime<0:
                print("Invalid Input!basic hours cannot be over 20 hours or less than 0")
                print()
                friday_overtime=int(input("Enter friday Overtime Hours:"))
                print()

            friday_overtime_pay=friday_overtime*1.5*overtime_rate

            holiday_overtime=int(input("Enter holiday Overtime Hours:"))          #Holiday Overtime
            print()
            
            while holiday_overtime>20 or holiday_overtime<0:
                print("Invalid Input!basic hours cannot be over 20 hours or less than 0")
                print()
                holiday_overtime=int(input("Enter holiday Overtime Hours:"))
                print()

            holiday_overtime_pay=holiday_overtime*2.5*overtime_rate

            #salary
            salary=basic_pay+normal_overtime_pay+friday_overtime_pay+holiday_overtime_pay
            
            sql=("INSERT into salary values(%s,%s,%s,%s,%s,%s,%s,%s)")
            val=[id, month, year, hours, normal_overtime, friday_overtime, holiday_overtime, salary]
            print(val)
            x.execute(sql,val)
            
            try:
                mydb.commit()
                print("Data has been added!")
                print('*'*50)
                print()
            except:
                mydb.rollback()

            x.close()
            mydb.close()
  
# Terminate

def terminate():
    loop=0
    while loop==0:
    
        id=int(input("Enter Employee Id to Terminate:"))
        print()
        
        import mysql.connector
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="employee")

        count=0
        x=mydb.cursor()
        x.execute("select Empid,Empname,Designation,Role,Status from empdata where Empid=%d"%id)
        rec=x.fetchall()
        
        for i in rec:
            count+=1
            data=i
            
        if count==0:
            print("No data found!")
            print()
            
        elif count==1:
            
            if data[4]=='t' or data[4]=='T':
                print("This user has already been Terminated")
                print('*'*50)
                print()
                
            else:
                print(data)
                print()

                loopt=0
                while loopt==0:
                    
                    print("Eployee:",id,"- Status will be changed to Terminated(T)!")
                    confirm=input("Do you wish to continue?(yes/no):")
                    print()
                
                    if confirm.lower()=='yes':
                        x.execute("update empdata set status='T' where Empid=%d"%data[0])

                        try:
                            mydb.commit()
                            print("Employee:",id,"-Status changed to Terminated(T)!")
                            print('*'*50)
                            print()
                        
                        except:
                            mydb.rollback()

                        x.close()
                        mydb.close()
                        loopt=1

                    elif confirm.lower()=='no':
                        loopt=1
                        print("Employee:",id,"-Status is still Active")
                        print()

        loopc=0
        while loopc==0:

            cont=input("Do you want to continue(yes/no):")
            print()
            print('*'*50)
            print()
            
            if cont.lower()=='yes':
                loopc=1

            elif cont.lower()=='no':
                loop=1
                loopc=1
                    

#Update Empdata

def update_emp():

    id=int(input("Enter Employee Id:"))
    print()
    
    
    loopc=0
    loop=0
    while loop==0:
        import mysql.connector
        mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="root",
         database="employee")

        count=0
        x=mydb.cursor()
        x.execute("select * from empdata where Empid=%d"%id)
        rec=x.fetchall()
            
        for i in rec:
            count+=1
            print(i)
            print()
            emp=i
            #emp=[Empid, Empname, Designation, Role, status, password, basic, allowence]
        
        if count==0:
            print("No data found!")
            loop=1
            print()

        else:
        
            print("1.Empname: ",emp[1])
            print()
            print("2.Designation: ",emp[2])
            print()
            print("3.Role(Admin-'A'/User-'U'/Manager-'M'): ",emp[3],)
            print()
            print("4.status(Active-'A'/Terminated-'T'): ",emp[4])
            print()
            print("5.password: ",emp[5])
            print()
            print("6.basic: ",emp[6])
            print()
            print("7.allowence: ",emp[7])
            print()
            print("8.Exit")
            print()

            print("Enter one feild at a time!")
            ch=int(input("Enter Feild for Updation (1/2/.../8):"))
            print()

            if ch==8:
                loop=1
                loopc=1
                print('*'*50)
                print()
                break

            elif ch==1:
                
                name=input("Enter Updated name:")
                print()

                sql=("update empdata set Empname=%s where Empid=%s")
                val=[name,id]
                x.execute(sql,val)

                try:
                    mydb.commit()
                    print("Empname:",name,"-Updated!")
                    print('*'*50)
                    print()
                        
                except:
                    mydb.rollback()

                x.close()
                mydb.close()

            elif ch==2:
                
                Designation=input("Enter Updated Designation:")
                print()

                sql=("update empdata set Designation=%s where Empid=%s")
                val=[Designation,id]
                x.execute(sql,val)

                try:
                    mydb.commit()
                    print("Designation:",Designation,"-Updated!")
                    print('*'*50)
                    print()
                        
                except:
                    mydb.rollback()

                x.close()
                mydb.close()

            elif ch==3:

                r=['U','A','M']
                Role=input("Enter Updated Role (Admin-'A'/User-'U'/Manager-'M'):")
                Role=Role.upper()
                print()
                while Role not in r:
                    print("Role will only take the vales:",r)
                    print()
                    Role=input("Enter Updated Role (Admin-'A'/User-'U'/Manager-'M'):")
                    Role=Role.upper()
                    print()
                print()

                sql=("update empdata set Role=%s where Empid=%s")
                val=[Role,id]
                x.execute(sql,val)

                try:
                    mydb.commit()
                    print("Role:",Role,"-Updated!")
                    print('*'*50)
                    print()
                        
                except:
                    mydb.rollback()

                x.close()
                mydb.close()

            elif ch==4:

                s=['A','T']
                status=input("Enter Updated Status(Active-'A'/Terminated-'T'):")
                status=status.upper()
                print()
                while status not in s:
                    print("Status will only takes the vales as:",s)
                    status=input("Enter Updated Status(Active-'A'/Terminated-'T'):")
                    status=status.upper()
                    print()
                print()

                sql=("update empdata set status=%s where Empid=%s")
                val=[status,id]
                x.execute(sql,val)

                try:
                    mydb.commit()
                    print("status:",status,"-Updated!")
                    print('*'*50)
                    print()
                        
                except:
                    mydb.rollback()

                x.close()
                mydb.close()

            elif ch==5:
                
                password=input("Enter Updated Password:")
                print()

                sql=("update empdata set password=%s where Empid=%s")
                val=[password,id]
                x.execute(sql,val)

                try:
                    mydb.commit()
                    print("password:",password,"-Updated!")
                    print('*'*50)
                    print()
                        
                except:
                    mydb.rollback()

                x.close()
                mydb.close()

            elif ch==6:
                
                basic=float(input("Enter Updated Basic Salary:"))
                print()

                sql=("update empdata set basic=%s where Empid=%s")
                val=[basic,id]
                x.execute(sql,val)

                try:
                    mydb.commit()
                    print("basic:",basic,"-Updated!")
                    print('*'*50)
                    print()
                        
                except:
                    mydb.rollback()

                x.close()
                mydb.close()
                
            elif ch==7:
                
                allowence=float(input("Enter Updated Allowence:"))
                print()

                sql=("update empdata set allowence=%s where Empid=%s")
                val=[allowence,id]
                x.execute(sql,val)

                try:
                    mydb.commit()
                    print("allowence:",allowence,"-Updated!")
                    print('*'*50)
                    print()
                        
                except:
                    mydb.rollback()

                x.close()
                mydb.close()

        
        while loopc==0:
            cont=input("Do you want to continue(yes/no):")
            print()
            print('*'*50)
            if cont.lower()=='yes':
                loopc=1
                
            elif cont.lower()=='no':
                loopc=1
                loop=1
                
                break


#Update salary

def update_sal():

    l=0
    while l==0:

        import mysql.connector
        mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="root",
         database="employee")
        x=mydb.cursor()
    
        id=int(input("Enter Employee Id:"))
        print()
        
        ci=0
        x.execute("select * from salary where Empid=%d"%id)
        rec=x.fetchall()
        
        for i in rec:
            ci+=1
            print(i)
            print()
            
        if ci==0:
            print("No data found!")
            print()
            print('*'*50)
            print()
            loop=1
            break
           
        month=input("Enter Month:")
        print()
        year=input("Enter Year:")
        print()

        c=0
        x=mydb.cursor()
        sql=("select basic,allowence from empdata where Empid=%s")
        val=[id]
        x.execute(sql,val)
        rec=x.fetchall()
        
        for i in rec:
            c+=1
            data=i
            
        if c==0:
            print("Empid not found!")
            print()
            loop=1
            break
            
        basic=data[0]
        allowence=data[1]

        basic_rate=(basic+allowence)/240            #basic rate
        overtime_rate=basic/240                     #over time rate
        
        loop=0
        while loop==0:
            
            import mysql.connector
            mydb = mysql.connector.connect(
             host="localhost",
             user="root",
             password="root",
             database="employee")
            x=mydb.cursor()
            
            count=0
            
            sql=("select * from salary where Empid=%s and month=%s and year=%s")
            val=[id,month,year]
            x.execute(sql,val)
            rec=x.fetchall()
            
            for i in rec:
                count+=1
                print(i)
                print()
                emp=i
                #emp=[Empid, month, year, basic_hours, normal_overtime, friday_overtime, holiday_overtime, salary]


            if count==0:
                print("No data found!")
                print()
                print('*'*50)
                loop=1
                l=1
                print()
                break

            
            print("1.month: ",emp[1])
            print()
            print("2.year: ",emp[2])
            print()
            print("3.basic_hours: ",emp[3])
            print()
            print("4.normal_overtime: ",emp[4])
            print()
            print("5.friday_overtime: ",emp[5])
            print()
            print("6.holiday_overtime: ",emp[6])
            print()
            print("7.Exit")
            print()

            print("Enter one feild at a time!")
            ch=int(input("Enter Feild for Updation (1/2/.../7):"))
            print()

            #Exit
            if ch==7:
                loop=1
                l=1
                print('*'*50)
                print()
                break

            #month
            elif ch==1:

                import mysql.connector
                mydb = mysql.connector.connect(
                 host="localhost",
                 user="root",
                 password="root",
                 database="employee")
                x=mydb.cursor()
                    
                month=input("Enter Updated month:")
                print()

                sql=("update salary set month=%s where Empid=%s")
                val=[month,id]
                x.execute(sql,val)

                try:
                    mydb.commit()
                    print("month:",month,"-Updated!")
                    print('*'*50)
                    print()
                            
                except:
                    mydb.rollback()

                x.close()
                mydb.close()

            #year
            elif ch==2:

                import mysql.connector
                mydb = mysql.connector.connect(
                 host="localhost",
                 user="root",
                 password="root",
                 database="employee")
                x=mydb.cursor()
                
                year=int(input("Enter Updated year:"))
                print()

                sql=("update salary set year=%s where Empid=%s")
                val=[year,id]
                x.execute(sql,val)

                try:
                    mydb.commit()
                    print("year:",year,"-Updated!")
                    print('*'*50)
                    print()
                            
                except:
                    mydb.rollback()

                x.close()
                mydb.close()
            
            #basic_hours
            elif ch==3:

                import mysql.connector
                mydb = mysql.connector.connect(
                 host="localhost",
                 user="root",
                 password="root",
                 database="employee")
                x=mydb.cursor()

                hours=float(input("Enter Updatede Basic Hours:"))     #Normal Hours
                print()
        
                while hours>240 or hours<0:
                    print("Invalid Input!basic hours cannot be over 240 hours or less than 0")
                    print()
                    hours=float(input("Enter Basic Hours Worked:"))
                    print()

                sql=("update salary set basic_hours=%s where Empid=%s")
                val=[hours,id]
                x.execute(sql,val)

                try:
                    mydb.commit()
                    print("basic_hours:",basic_hours,"-Updated!")
                    print('*'*50)
                    print()
                            
                except:
                    mydb.rollback()

                x.close()
                mydb.close()
                
            #normal overtime
            elif ch==4:

                import mysql.connector
                mydb = mysql.connector.connect(
                 host="localhost",
                 user="root",
                 password="root",
                 database="employee")
                x=mydb.cursor()

                normal_overtime=float(input("Enter Updated normal_overtime Hours:"))     #Normal Hours
                print()
        
                while normal_overtime>72 or normal_overtime<0:
                    print("Invalid Input!basic overtime hours cannot be over 72 hours or less than 0") #check value of normal overtime hours
                    print()
                    normal_overtime=int(input("Enter Updated Normal Overtime Hours:"))
                    print()

                

                sql=("update salary set normal_overtime=%s where Empid=%s")
                val=[normal_overtime,id]
                x.execute(sql,val)

                try:
                    mydb.commit()
                    print("normal_overtime:",normal_overtime,"-Updated!")
                    print('*'*50)
                    print()
                            
                except:
                    mydb.rollback()

                x.close()
                mydb.close()

            elif ch==5:

                import mysql.connector
                mydb = mysql.connector.connect(
                 host="localhost",
                 user="root",
                 password="root",
                 database="employee")
                x=mydb.cursor()
                
                friday_overtime=int(input("Enter friday Overtime Hours:"))          #Friday Overtime
                print()
        
                while friday_overtime>20 or friday_overtime<0:
                    print("Invalid Input!basic hours cannot be over 20 hours or less than 0")
                    print()
                    friday_overtime=int(input("Enter friday Overtime Hours:"))
                    print()

                friday_overtime_pay=friday_overtime*1.5*overtime_rate

                sql=("update salary set friday_overtime=%s where Empid=%s")
                val=[friday_overtime,id]
                x.execute(sql,val)

                try:
                    mydb.commit()
                    print("friday_overtime:",friday_overtime,"-Updated!")
                    print('*'*50)
                    print()
                            
                except:
                    mydb.rollback()

                x.close()
                mydb.close()

            elif ch==6:

                import mysql.connector
                mydb = mysql.connector.connect(
                 host="localhost",
                 user="root",
                 password="root",
                 database="employee")
                x=mydb.cursor()
                
                holiday_overtime=int(input("Enter holiday Overtime Hours:"))          #Holiday Overtime
                print()
        
                while holiday_overtime>20 or holiday_overtime<0:
                    print("Invalid Input!basic hours cannot be over 20 hours or less than 0")
                    print()
                    holiday_overtime=int(input("Enter holiday Overtime Hours:"))
                    print()

                holiday_overtime_pay=holiday_overtime*2.5*overtime_rate

                sql=("update salary set holiday_overtime=%s where Empid=%s")
                val=[holiday_overtime,id]
                x.execute(sql,val)

                try:
                    mydb.commit()
                    print("holiday_overtime:",holiday_overtime,"-Updated!")
                    print('*'*50)
                    print()
                            
                except:
                    mydb.rollback()

                x.close()
                mydb.close()

            #salary

            import mysql.connector
            mydb = mysql.connector.connect(
             host="localhost",
             user="root",
             password="root",
             database="employee")
            x=mydb.cursor()
            
            sql=("select basic_hours,normal_overtime,friday_overtime,holiday_overtime from salary where Empid=%s and month=%s and year=%s")
            val=[id,month,year]
            x.execute(sql,val)
            rec=x.fetchall()
        
            for i in rec:
                saldata=i
                #saldata=[basic_hours,normal_overtime,friday_overtime,holiday_overtime]
                print()
            
            if len(saldata)==0:
                loop=1
                print()
                break
            
            basic_pay=saldata[0]*basic_rate

            normal_overtime_pay=saldata[1]*1.25*overtime_rate

            friday_overtime_pay=saldata[2]*1.5*overtime_rate

            holiday_overtime_pay=saldata[3]*2.5*overtime_rate
            
            salary=basic_pay+normal_overtime_pay+friday_overtime_pay+holiday_overtime_pay
            
            sql=("update salary set salary=%s where Empid=%s")
            val=[salary,id]
            x.execute(sql,val)

            try:
                mydb.commit()
                print("salary:",salary,"-Updated!")
                print('*'*50)
                print()
                            
            except:
                mydb.rollback()

            x.close()
            mydb.close()

#delete function

def delete():

    loop=0
    loopc=0
    while loop==0:
        
        import mysql.connector
        mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="root",
         database="employee")
        
        x=mydb.cursor()
        
        print("1.Delete empdata")
        print()
        print("2.Delete All Salary Data of an Employee")
        print()
        print("3.Delete Specific Salary Data of an Employee")
        print()
        print("4.Back")
        print()
        
        ch=int(input("Enter choice:"))
        print()
        print('*'*50)
        print()
        
        if ch==4:
            
            loop=1
            loopc=1
            print('*'*50)
            print()

                
        elif ch==1:

            loope=0
            while loope==0:
                
                id=int(input("Enter Employee Id to be Deleted:"))
                print()

                ci=specific_empdata(id)
                    
                if ci==0:
                    
                    print()
                    loope=0
                    break
                

                print("Eployee:",id,"- All Empdata and Salary Data will be Deleted!!")
                confirm=input("Do you wish to continue?(yes/no):")
                print()
                
                if confirm.lower()=='yes':
                
                    x.execute("delete from salary where Empid=%d"%id)
                    x.execute("delete from empdata where Empid=%d"%id)

                    try:
                        mydb.commit()
                        print("Employee Id:",id,"-Deleted!")
                        print('*'*50)
                        print()
                        loope=1
                        
                    except:
                        mydb.rollback()

                    x.close()
                    mydb.close()

                elif confirm.lower()=='no':
                    
                    print("Employee Id:",id,"-Has not been Deleted!")
                    print('*'*50)
                    print()
                    
        elif ch==2:
            
            loopa=0
            while loopa==0:
                
                id=int(input("Enter Employee Id to Delete All Salary Data:"))
                print()

                ci=specific_salary(id)
                
                if ci==0:
                    print()
                    loopa=1
                    break

                print("Eployee:",id,"- All Salary Data will be Deleted!!")
                confirm=input("Do you wish to continue?(yes/no):")
                print()
                
                if confirm.lower()=='yes':
                
                    x.execute("delete from salary where Empid=%d"%id)

                    try:
                        mydb.commit()
                        print("Employee Id:",id,"-Salary Data Deleted!")
                        print('*'*50)
                        print()
                        loopa=1
                        
                    except:
                        mydb.rollback()

                    x.close()
                    mydb.close()

                elif confirm.lower()=='no':
                    
                    print("Employee Id:",id,"-Salary Data Has not been Deleted!")
                    print('*'*50)
                    print()
                    loopa=0

        elif ch==3:

            loops=0
            while loops==0:
                
                id=int(input("Enter Employee Id to Delete Salary Data:"))
                print()

            
                out=specific_salary(id)
                if out==0:
                    loops=1
                    break

                month=input("Enter Month:")
                print()
                year=int(input("Enter Year:"))
                print()

                count=0
                x=mydb.cursor()
                
                sql=("select * from salary where Empid=%s and month=%s and year=%s")
                val=[id,month,year]
                x.execute(sql,val)
                rec=x.fetchall()
                
                for i in rec:
                    
                    count+=1
                    print()
                    emp=i
                    #emp=[Empid, month, year, basic_hours, normal_overtime, friday_overtime, holiday_overtime, salary]


                if count==0:
                    
                    print("No data found!")
                    print()
                    print('*'*50)
                    loops=1
                    print()
                    break

                else:
                    
                    print("Eployee:",id,"Month:",month,"Year:",year,"- Salary Data will be Deleted!")
                    confirm=input("Do you wish to continue?(yes/no):")
                    print()
                    
                    if confirm.lower()=='yes':
                    
                        sql=("delete from salary where Empid=%s and month=%s and year=%s")
                        val=[id,month,year]
                        x.execute(sql,val)

                        try:
                            mydb.commit()
                            print("Employee Id:",id,"Month:",month,"Year:",year,"-Salary Data Deleted!")
                            print('*'*50)
                            print()
                            loops=1
                            
                        except:
                            mydb.rollback()

                        x.close()
                        mydb.close()

                    elif confirm.lower()=='no':
                        
                        print("Employee Id:",id,"Month:",month,"Year:",year,"-Salary Data Has not been Deleted!")
                        print('*'*50)
                        print()
                        loops=1
                    
        
        while loopc==0:
                    
            cont=input("Do You wish to Continue(yes/no):")
            print()
            print('*'*50)
            print()
            if cont.lower()=='yes':
                loopc=1
                loop=0

            elif cont.lower()=='no':
                loop=1
                loopc=1
                        
def view():

    loopv=0
    while loopv==0:
        
        loopc=0
        print("1.View Employee Data")
        print()
        print("2.View specific Employee Data")
        print()
        print("3.View Salary Data")
        print()
        print("4.view Specific Salary Data")
        print()
        print("5.Back")
        print()

        ch=int(input("Enter Choice(1/2/../5):"))
        print()
        print('*'*50)
        print()
        
        if ch==1:
            empdata()

        elif ch==2:
            id=int(input("Enter Empid:"))
            print()
            specific_empdata(id)

        elif ch==3:
            salary()

        elif ch==4:
            id=int(input("Enter Empid:"))
            print()
            specific_salary(id)

        elif ch==5:
            loopc=1
            #back()
            break
        
        while loopc==0:

            cont=input("Do you want to continue(yes/no):")
            print()
            print('*'*50)
            print()

            if cont.lower()=='yes':
                loopc=1

            elif cont.lower()=='no':
                loopv=1
                loopc=1

def add():

    loop=0
    while loop==0:
        
        print("1.Add New Employee Data")
        print()
        print("2.Add New Salary data")
        print()
        print("3.Back")
        print()

        ch=int(input("Enter Choice(1/2/3):"))
        print()
        print('*'*50)
        print()

        if ch==1:
            addemp()

        elif ch==2:
            addsal()

        elif ch==3:
            #back()
            break

        loopc=0
        while loopc==0:
            cont=input("Do you want to continue(yes/no):")
            print()
            print('*'*50)
            print()
            
            if cont.lower()=='yes':
                loopc=1
                
            elif cont.lower()=='no':
                loopc=1
                loop=1
            
def update():

    loop=0
    while loop==0:
        print("1.Update Empdata")
        print()
        print("2.Update Salary Data")
        print()
        print("3.back")
        print()
        
        ch=int(input("Enter Choice(1/2/3):"))
        print()
        print('*'*50)
        print()
        
        if ch==1:
            update_emp()

        elif ch==2:
            update_sal()
                     
        elif ch==3:
            #back()
            loop=0
            break

        
            
def execute(role,loginid):
    if role=='u' or role=='U':
        print("Welcome! you are a User.")
        print()
        user(loginid)
    elif role=='m' or role=='M':
        print("Welcome! you are a Manager.")
        print()
        manager(loginid)
    elif role=='a' or role=='A':
        print("Welcome! you are an Admin.")
        print()
        admin(loginid)
        

#change password function
def password(id):

    import mysql.connector
    mydb = mysql.connector.connect(
             host="localhost",
             user="root",
             password="root",
             database="employee")
    x=mydb.cursor()

    ok=0
    old=input("Enter old Password:")
    
    x.execute("select Empid,password,Role,status from empdata where Empid=%d"%id)
    rec=x.fetchall()
    for i in rec:
                        
        if i[0]==id and i[1]==old:
            print("Correct Password!")
            print()
            login=i
            print()
            ok=1
                                  
        else:
            print("Incorrect Password!Try Again")
            print()
    
    if ok==1:
        pnew=input("Enter New Password:")
        print()
        pnewcon=input("Confirm New Passwrod:")
        print()
                
        if pnew==pnewcon:
            
            sql=("update empdata set password=%s where Empid=%s")
            val=[pnew,id]
            x.execute(sql,val)

            try:
                mydb.commit()
                print("New Password:",pnew,"-Updated!")
                print('*'*50)
                print()
                
            except:
                mydb.rollback()
                    

            x.close()
            mydb.close()
            
        else:
            print()
            print("The passwords do no match! Please  enter the same password!")
            print()
            print('*'*50)
            print()
        

# run()

def run():
    
    log=login()
    if log[0] in [0]:
        print("Exiting!")
    else:

        loginid=log[0]
        role=log[2]
        execute(role,loginid)


run()


    

            
    



    
