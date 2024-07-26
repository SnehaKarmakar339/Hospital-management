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
                                      
                           #Enter a new record
                           elif b==2:
                                print('''
                                           1) Doctor details
                                           2) Nurse details
                                           3) Others staff
                                                                ''')
                                
                                c=int(input("Enter your choice:"))
                                #Enter doctor details
                                if c==1:
                                    #inputting the details
                                    reg=input("Enter the liscence number: ")
                                    name=input("Enter the doctors name:")
                                    spe=input("Enter the specialization:")
                                    age=input("Enter the age:")
                                    add=input("Enter the address:")
                                    con=input("Enter the contact:")
                                    fees=input("Enter the fees:")
                                    ms=input("Enter the salary:")
                                    #inserting values in doctor details
                                    cursor.execute("insert into doctor_details values('"+reg+"','"+name+"','"+spe+"','"+age+"','"+add+"','"+con+"','"+fees+"','"+ms+"')")
                                    mysql.commit()
                                    print("SUCCESSFULLY ADDED")
                                #Enter nurse details
                                elif c==2:
                                    #inputting the values
                                    name=input("Enter the name:")
                                    age=input("Enter the age:")
                                    add=input("Enter the address:")
                                    con=input("Enter the contact:")
                                    ms=input("Enter the monthly salary:")
                                    #inserting values in nurse details
                                    cursor.execute("insert into nurse_details values('"+name+"','"+age+"','"+add+"','"+con+"','"+ms+"')")
                                    mysql.commit()
                                    print("SUCCESSFULLY ADDED")
                                #enter worker details
                                elif c==3:
                                    #inputting values
                                    name=input("Enter the name:")
                                    age=input("Enter the age:")
                                    add=input("Enter the address:")
                                    con=input("Enter the contact:")
                                    ms=input("Enter the monthly salary:")
                                    #inserting values in worker details
                                    cursor.execute("insert into other_staff_details values('"+name+"','"+age+"','"+add+"','"+con+"','"+ms+"')")
                                    mysql.commit()
                                    print("SUCCESSFULLY ADDED")
                           #Updating details
                           elif b==3:
                                print('''
                                           1) Doctor details
                                           2) Nurse details
                                           3) Other staff

                                                             ''')
                                c=int(input("Enter your choice:"))
                                #Updating Doctor's details
                                if c==1:
                                    name=input("Enter the name of the doctor you want to update:")
                                    cursor.execute("select*from doctor_details where name='"+name+"'")
                                    r=cursor.fetchall()
                                    print(r)
                                    print(''' Enter the number for the respective choice to update it:
                                                1) age
                                                2) address
                                                3) contact
                                                4) fees
                                                5) monthly salary
                                                                             ''')
                                    d=int(input("Enter your choice:"))
                                    if d==1:#Changing age                                                                   
                                        age=input("Enter the new age:")
                                        cursor.execute("update doctor_details set age='"+age+"' where name='"+name+"'")
                                        mysql.commit()
                                        print("The age has been updated!")
                                        print()
                                        cursor.execute("select*from doctor_details where name='"+name+"'")
                                        e=cursor.fetchall()
                                        print(e)
                                    
                                    elif d==2:#Changing address
                                        print("!!!Please dont enter more than 30 characters!!!")
                                        add=input("Enter new address:")
                                        cursor.execute("update doctor_details set address='"+add+"' where name='"+name+"'")
                                        mysql.commit()
                                        print("!!!The address has been updated!!!")
                                        print()
                                        cursor.execute("select*from doctor_details where name='"+name+"'")
                                        e=cursor.fetchall()
                                        print(e)                                        
                                    elif d==3:#changing contact number
                                        print("!!!Please dont enter more than 10 characters!!!")
                                        cont=input("Enter new contact number:")
                                        cursor.execute("update doctor_details set contact='"+cont+"' where name='"+name+"'")
                                        mysql.commit()
                                        print("!!!The contact has been updated!!!")
                                        print()
                                        cursor.execute("select*from doctor_details where name='"+name+"'")
                                        e=cursor.fetchall()
                                        print(e)          
                                    elif d==4: #Changing fees
                                        print("!!!Please dont enter more than 5 characters!!!")
                                        fee=input("Enter new assigned fees:")
                                        cursor.execute("update doctor_details set fees='"+fee+"' where name='"+name+"'")
                                        mysql.commit()
                                        print("!!!The fees has been updated!!!")
                                        print()
                                        cursor.execute("select*from doctor_details where name='"+name+"'")
                                        e=cursor.fetchall()
                                        print(e)      
                                    elif d==5:#Changing salary 
                                        print("!!!Please dont enter more than 10 characters!!!")
                                        sal=input("Enter new assigned salary:")
                                        cursor.execute("update doctor_details set monthly_salary='"+sal+"' where name='"+name+"'")
                                        mysql.commit()
                                        print("!!!The monthly salary has been updated!!!")
                                        print()
                                        cursor.execute("select*from doctor_details where name='"+name+"'")
                                        e=cursor.fetchall()
                                        print(e)      
                                #Updating Nurses details       
                                elif c==2:
                                    name=input("Enter the name of the nurse you want to update:")
                                    cursor.execute("select*from nurse_details where name='"+name+"'")
                                    r=cursor.fetchall()
                                    print(r)
                                    print(''' Enter the number for the respective choice to update it:
                                                1) age
                                                2) address
                                                3) contact
                                                4) monthly salary
                                                                             ''')
                                    d=int(input("Enter your choice:"))
                                    if d==1:#Changing age                                                                   
                                        age=input("Enter the new age:")
                                        cursor.execute("update nurse_details set age='"+age+"' where name='"+name+"'")
                                        mysql.commit()
                                        print("The age has been updated!")
                                        print()
                                        cursor.execute("select*from nurse_details where name='"+name+"'")
                                        e=cursor.fetchall()
                                        print(e)
                                    
                                    elif d==2:#Changing address
                                        print("!!!Please dont enter more than 30 characters!!!")
                                        add=input("Enter new address:")
                                        cursor.execute("update nurse_details set address='"+add+"' where name='"+name+"'")
                                        mysql.commit()
                                        print("!!!The address has been updated!!!")
                                        print()
                                        cursor.execute("select*from nurse_details where name='"+name+"'")
                                        e=cursor.fetchall()
                                        print(e)                                        
                                    elif d==3:#changing contact number
                                        print("!!!Please dont enter more than 10 characters!!!")
                                        cont=input("Enter new contact number:")
                                        cursor.execute("update nurse_details set contact='"+cont+"' where name='"+name+"'")
                                        mysql.commit()
                                        print("!!!The contact has been updated!!!")
                                        print()
                                        cursor.execute("select*from nurse_details where name='"+name+"'")
                                        e=cursor.fetchall()
                                        print(e)            
                                    elif d==4:#Changing salary 
                                        print("!!!Please dont enter more than 10 characters!!!")
                                        sal=input("Enter new assigned salary:")
                                        cursor.execute("update nurse_details set monthly_salary='"+sal+"' where name='"+name+"'")
                                        mysql.commit()
                                        print("!!!The monthly salary has been updated!!!")
                                        print()
                                        cursor.execute("select*from nurse_details where name='"+name+"'")
                                        e=cursor.fetchall()
                                        print(e)      
                                #Updating other staff's details
                                elif c==3: 
                                    name=input("Enter the name of the staff you want to update:")
                                    cursor.execute("select*from other_staff_details where name='"+name+"'")
                                    r=cursor.fetchall()
                                    print(r)
                                    print(''' Enter the number for the respective choice to update it:
                                                1) age
                                                2) address
                                                3) contact
                                                4) monthly salary
                                                                             ''')
                                    d=int(input("Enter your choice:"))
                                    if d==1:#Changing age                                                                   
                                        age=input("Enter the new age:")
                                        cursor.execute("update other_staff_details set age='"+age+"' where name='"+name+"'")
                                        mysql.commit()
                                        print("The age has been updated!")
                                        print()
                                        cursor.execute("select*from other_staff_details where name='"+name+"'")
                                        e=cursor.fetchall()
                                        print(e)
                                    
                                    elif d==2:#Changing address
                                        print("!!!Please dont enter more than 30 characters!!!")
                                        add=input("Enter new address:")
                                        cursor.execute("update other_staff_details set address='"+add+"' where name='"+name+"'")
                                        mysql.commit()
                                        print("!!!The address has been updated!!!")
                                        print()
                                        cursor.execute("select*from other_staff_details where name='"+name+"'")
                                        e=cursor.fetchall()
                                        print(e)                                        
                                    elif d==3:#changing contact number
                                        print("!!!Please dont enter more than 10 characters!!!")
                                        cont=input("Enter new contact number:")
                                        cursor.execute("update other_staff_details set contact='"+cont+"' where name='"+name+"'")
                                        mysql.commit()
                                        print("!!!The contact has been updated!!!")
                                        print()
                                        cursor.execute("select*from other_staff_details where name='"+name+"'")
                                        e=cursor.fetchall()
                                        print(e)            
                                    elif d==4:#Changing salary 
                                        print("!!!Please dont enter more than 10 characters!!!")
                                        sal=input("Enter new assigned salary:")
                                        cursor.execute("update other_staff_details set monthly_salary='"+sal+"' where name='"+name+"'")
                                        mysql.commit()
                                        print("!!!The monthly salary has been updated!!!")
                                        print()
                                        cursor.execute("select*from other_staff_details where name='"+name+"'")
                                        e=cursor.fetchall()
                                        print(e)      
                           #deleting a member        
                           elif b==4:   
                                print('''
                                           1) Doctor details
                                           2) Nurse details
                                           3) others staff
                                                          ''')
                                c=int(input("Enter your choice:"))
                                #deleting doctors details
                                if c==1:
                                    name=input("Enter doctors name:")
                                    cursor.execute("select*from doctor_details where name='"+name+"'")
                                    row=cursor.fetchall()
                                    print(row)
                                    p=input("you really wanna delete this data? (y/n):")
                                    if p=="y":
                                        cursor.execute("delete from doctor_details where name='"+name+"'")
                                        mysql.commit()
                                        print("SUCCESSFULLY DELETED!!")
                                    else:
                                        print("NOT DELETED")
                                #deleting nurse details
                                elif c==2:
                                    name=input("Enter nurse name:")
                                    cursor.execute("select*from nurse_details where name='"+name+"'")
                                    row=cursor.fetchall()
                                    print(row)
                                    p=input("you really wanna delete this data? (y/n):")
                                    if p=="y":
                                        cursor.execute("delete from nurse_details where name='"+name+"'")
                                        mysql.commit()
                                        print("SUCCESSFULLY DELETED!!")
                                    else:
                                        print("NOT DELETED")
                                #deleting worker details
                                elif c==3:
                                    name=input("Enter workers name:")
                                    cursor.execute("select*from other_staff_details where name='"+name+"'")
                                    row=cursor.fetchall()
                                    print(row)
                                    p=input("you really wanna delete this data? (y/n):")
                                    if p=="y":
                                        cursor.execute("delete from other_staff_details where name='"+name+"'")
                                        mysql.commit()
                                        print("SUCCESSFULLY DELETED!!")
                                    else:
                                        print("NOT DELETED")
                           elif b==5:
                                break