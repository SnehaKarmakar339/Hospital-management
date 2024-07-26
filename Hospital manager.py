while True:
    print('''

        ===========================
           WELCOME TO CITYHOSPITAL
        ===========================


                ''')
    #Creating database connectivity
    import mysql.connector
    passd=str(input("Enter the database password please:"))
    mysql= mysql.connector.connect(host='localhost',user='root',password=passd)
    cursor=mysql.cursor()
    cursor.execute("create database if not exists city_hospital")
    cursor.execute("use city_hospital")
    #creating required tables
    cursor.execute("create table if not exists patient_details(name varchar(30),sex varchar(3),age int(3),diagnosed_illness varchar(30),address varchar(50),contact varchar(15))")
    cursor.execute("create table if not exists doctor_details(reg_no int(5) primary key,name varchar(30), specialisation varchar(40),age int(2),address varchar(30),contact varchar(15),fees int(10),monthly_salary int(10))")
    cursor.execute("create table if not exists nurse_details(name varchar(30),age int(2),address varchar(30),contact varchar(15),monthly_salary int(10))")
    cursor.execute("create table if not exists other_staff_details(name varchar(30),age int(2),address varchar(30),contact varchar(15),monthly_salary int(10))")
    #creating tables for storing the username and password of the user
    cursor.execute("create table if not exists user_data(username varchar(30), password varchar(30) primary key)")

    while True:
        print( '''
                   1) Sign in
                   2) Registration
                                    ''')
    
        r=int(input("Enter your choice:"))
        if r==2:
            print('''
                         ==================================
                                REGISTER YOURSELF
                         ==================================
                                                                ''')
            u=input("input your username:")
            p=input("input the password(the password must be strong!!):")
            cursor.execute("insert into user_data values('"+u+"','"+p+"')")
            mysql.commit()

            print('''
                          ================================================
                           YOUR REGISTRATION HAS BEEN DONE SUCCESSFULLY!!
                          ================================================
                                                                              ''')
            x=input("enter any key to continue:")
        # if user wants to login
        elif r==1:
            print('''
                        ===================================
                          !!!!!!!!!!!SIGN IN!!!!!!!!!!!!
                      ===================================
                                                        ''')
            un=input("Enter username:")
            ps=input("password:")

            cursor.execute("select password from user_data where username='" +un+ "' ")
            row = cursor.fetchall()
            for i in row:
               a=list(i)
               if a[0]==str(ps):
                   while True:
                       print('''
                              1) Administration
                              2) patient 
                              3) Sign Out
                                         ''')
                       a=int(input("Enter your choice:"))
                       #Administration
                       if a==1:
                           print('''
                                        1) Display the details
                                        2) Add a new member
                                        3) Updating details
                                        4) Delete a member
                                        5) Exit
                                                   ''')
                           b=int(input("Enter your choice:"))
                           #Display Details
                           if b==1:
                              print('''
                                        1) Doctor details
                                        2) Nurse details
                                        3) Other staff
                                                        ''')
                              c=int(input("Enter your choice:"))
                             
                              if c==1:
                                   print('''

                                              1) Details of all doctors
                                              2) Details of a specific doctor


                                                                               ''')
                                   h=int(input("Enter your choice:"))
                                   if h==1:
                                      cursor.execute("select*from doctor_details")
                                      row=cursor.fetchall()
                                      for i in row:
                                         v=list(i)
                                         k=["REGNO","NAME","SPECIALISATION","AGE","ADDRESS","CONTACT","FEES","MONTHLY_SALARY"]
                                         d=dict(zip(k,v))
                                         print(d)
                                   elif h==2:
                                       n=input("Enter the name of the doctor you want to display:")
                                       cursor.execute("select*from doctor_details where name='"+n+"'")
                                       s=cursor.fetchone()
                                       p=list(s)
                                       k=["REGNO","NAME","SPECIALISATION","AGE","ADDRESS","CONTACT","FEES","MONTHLY_SALARY"]
                                       d=dict(zip(k,p))
                                       print(d)
                                       
                                       
                                    #display nurse details
                              elif c==2:
                                  print('''

                                                 1) Details of all the nurses
                                                 2) Details of a specific nurse   


                                                                                    ''')
                                  h=int(input("Enter your choice:"))
                                  if h==1:
                                      cursor.execute("select*from nurse_details")
                                      row=cursor.fetchall()
                                      for i in row:
                                          v=list(i)
                                          k=["NAME","AGE","ADDRESS","CONTACT","MONTHLY_SALARY"]
                                          d=dict(zip(k,v))
                                          print(d)
                                  elif h==2:
                                       n=input("Enter the name of the nurse you want to display:")
                                       cursor.execute("select*from nurse_details where name='"+n+"'")
                                       s=cursor.fetchone()
                                       p=list(s)
                                       k=("NAME","AGE","ADDRESS","CONTACT","MONTHLY_SALARY")
                                       d=dict(zip(k,p))
                                       print(d)
                                      
                                    #displays worker details
                              elif c==3:
                                  print('''

                                               1) Details of all supporting staffs
                                               2) Details of a specific supporting staff

                                                                                                ''')
                                  h=int(input("Enter your choice:"))
                                  if h==1:
                                        cursor.execute("select*from other_staff_details")
                                        row=cursor.fetchall()
                                        for i in row:
                                            v=list(i)
                                            k=["NAME","AGE","ADDRESS","CONTACT","MONTHLY_SALARY"]
                                            d=dict(zip(k,v))
                                            print(d)
                                  elif h==2:
                                       n=input("Enter the name of the supporting staff u want to display:")
                                       cursor.execute("select*from other_staff_details where name='"+n+"'")
                                       s=cursor.fetchone()
                                       p=list(s)
                                       k=["NAME","AGE","ADDRESS","CONTACT","MONTHLY_SALARY"]
                                       d=dict(zip(k,p))
                                       print(d)
                                      
