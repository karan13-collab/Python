#Python Program for a Car Showroom Management System


print("______________________________________________________________________________________________________________________________")
print()
print("                                           CAR SHOWROOM MANAGEMENT SYSTEM                                                     ")
print()
print("Created By: KARAN GHARDE")
print("GitHub Link: https://github.com/karan13-collab/")
print()
print()
print("______________________________________________________________________________________________________________________________")

#######################  Function to List All Cars  ##################
def listcar():
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",passwd="root",database="big_boy_carz")
    cursor=mycon.cursor()
    print("\n\nHERE ARE ALL THE CARS WE HAVE")
    cursor.execute("select brand,model,Seats,Engine_Type,Maximum_Speed,Maximum_Mileage,Colors,Price from cars")
    print("\n%18s"%"Brand","%18s"%"Model","%18s"%"Seats","%18s"%"Engine Type","%18s"%"Maximum Speed","%18s"%"Mileage","%18s"%"Colors","%18s"%"Price(in ₹)")
    cars=cursor.fetchall()
    for i in cars:
        for n in i:
            print("%18s"%n,end=" ")
        print()
    if cursor.rowcount==0:
        print("\n\nSorry, Currently We Have No Cars!")
    mycon.close()

#######################  Function to Find Cars By Integer Values  ##################
def findcarint(x,y):
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",passwd="root",database="big_boy_carz")
    cursor=mycon.cursor()
    query="select brand,model,Seats,Engine_Type,Maximum_Speed,Maximum_Mileage,Colors,Price from cars where {}>={}".format(x,y)
    cursor.execute(query)
    print("\n%18s"%"Brand","%18s"%"Model","%18s"%"Seats","%18s"%"Engine Type","%18s"%"Maximum Speed","%18s"%"Mileage","%18s"%"Colors","%18s"%"Price(in ₹)")
    cars=cursor.fetchall()
    for i in cars:
        for n in i:
            print("%18s"%n,end=" ")
        print()
    if cursor.rowcount==0:
        print("Sorry, ",x,y," Not Found")
    mycon.close()


#######################  Function to Find Cars By Strings ##################
def findcarstr(x,y):
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",passwd="root",database="big_boy_carz")
    cursor=mycon.cursor()
    query="select brand,model,Seats,Engine_Type,Maximum_Speed,Maximum_Mileage,Colors,Price from cars where {}='{}'".format(x,y)
    cursor.execute(query)
    print("\n%18s"%"Brand","%18s"%"Model","%18s"%"Seats","%18s"%"Engine Type","%18s"%"Maximum Speed","%18s"%"Mileage","%18s"%"Colors","%18s"%"Price(in ₹)")
    cars=cursor.fetchall()
    for i in cars:
        for n in i:
            print("%18s"%n,end=" ")
        print()
    if cursor.rowcount==0:
        print("Sorry, ",x,y," Not Found")
    mycon.close()

#######################  Function to Delete Cars  ##################
def delcar(x,y):
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",passwd="root",database="big_boy_carz")
    cursor=mycon.cursor()
    cursor.execute("DELETE from cars where Brand='{}' and Model='{}'".format(x,y))
    mycon.commit()
    print("\n\n",x,y," successfully deleted.")
    cho=int(input("\n\nWant To Display List Of Cars? \n1 For Yes \n2 For No\n"))
    if cho==1:
        cursor.execute("select brand,model,Seats,Engine_Type,Maximum_Speed,Maximum_Mileage,Colors,Price from cars")
        cars=cursor.fetchall()
        print("\n\n%18s"%"Brand","%18s"%"Model","%18s"%"Seats","%18s"%"Engine Type","%18s"%"Maximum Speed","%18s"%"Mileage","%18s"%"Colors","%18s"%"Price(in ₹)")
        for i in cars:
            for n in i:
                print("%18s"%n,end=" ")
            print()
    mycon.close()


#######################  Function to Add Cars  ##################
def addcar(a,b,c,d,e,f,g,h):
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",passwd="root",database="big_boy_carz")
    cursor=mycon.cursor()
    query="insert into cars values('{}','{}',{},'{}',{},{},'{}',{})".format(a,b,c,d,e,f,g,h)
    cursor.execute(query)
    mycon.commit()
    print("\n\n",a,b," added successfully.")
    cho=int(input("\n\nWant To Display List Of Cars? \n1 For Yes \n2 For No\n"))
    if cho==1:
        cursor.execute("select brand,model,Seats,Engine_Type,Maximum_Speed,Maximum_Mileage,Colors,Price from cars")
        cars=cursor.fetchall()
        print("\n\n%18s"%"Brand","%18s"%"Model","%18s"%"Seats","%18s"%"Engine Type","%18s"%"Maximum Speed","%18s"%"Mileage","%18s"%"Colors","%18s"%"Price(in ₹)")
        for i in cars:
            for n in i:
                print("%18s"%n,end=" ")
            print()
    mycon.close()

#######################  Function to Purchase Cars  ##################
def purchase(ab,bc,cd,de,ef,fg,gh):
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",passwd="root",database="big_boy_carz")
    cursor=mycon.cursor()
    cursor.execute("Select * from cars where Brand='{}' and Model='{}'".format(ef,fg))
    cars=cursor.fetchall()
    lis=[ab,bc,cd,de,gh]
    if cursor.rowcount==0:
        print("\n\nSorry, We Currently Don't Have ",ef,fg)
    else:
        for i in cars:
            for n in i:
                lis.append(n)
            with open("Customer.csv","a",newline='') as pur:
                purch=csv.writer(pur)
                payment=input("Payment Mode(Cash/Cheque/Card/Net Banking): ")
                lis.append(payment)
                purch.writerow(lis)
                print("\n\nPurchase Recorded!!!")
            pur.close()

#######################  Function to Find Cars In a Price Range ##################
def carprice(minp,maxp):
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",passwd="root",database="big_boy_carz")
    cursor=mycon.cursor()
    query="select brand,model,Seats,Engine_Type,Maximum_Speed,Maximum_Mileage,Colors,Price from cars where Price between {} and {}".format(minp,maxp)
    cursor.execute(query)
    print("\n\n%18s"%"Brand","%18s"%"Model","%18s"%"Seats","%18s"%"Engine Type","%18s"%"Maximum Speed","%18s"%"Mileage","%18s"%"Colors","%18s"%"Price(in ₹)")
    cars=cursor.fetchall()
    for i in cars:
        for n in i:
            print("18s"%n,end=" ")
        print()
    if cursor.rowcount==0:
        print("\n\nSorry, ",x,y," Not Found")
    mycon.close()



#___________MAIN PROGRAM___________#
import csv
visit=1

################  Main Menu ##############
while visit==1:
    print("\n\n*************************************************    Welcome to Big Boy Carz    **************************************************\n\n") 
    print("//////////////////////////////////////////////////////      Main Menu      //////////////////////////////////////////////////////\n\n\n")
    print("1. List All Cars")
    print("2. Add Cars")
    print("3. Delete Cars")
    print("4. Find Cars")
    print("5. Make A Purchase")
    print("6. Find A Purchase")
    choice=int(input("Select an Option: "))
    ans="y"
############ List cars ############
    if choice==1:
        listcar()
############ Add Car ############
    elif choice==2:                         
        while ans=="y" or ans=="Y":
            brand=input("\n\nEnter Brand Name: ")
            model=input("Enter Model: ")
            seat=int(input("Enter Number of Seats: "))
            engine=input("Enter Engine Type(Petrol/Diesel/CNG/EV): ")
            speed=int(input("Enter Maximum Speed(in km/h): "))
            mileage=int(input("Enter The Mileage(in km/l or km/charge): "))
            color=input("Enter Car Color(s)(Different Colors Separated By Comma): ")
            price=int(input("Enter The Price of The Car(in ₹): "))
            addcar(brand,model,seat,engine,speed,mileage,color,price)
            ans=input("\n\nWould You like to Add More Cars?(N/Y): ")
############ Delete Cars ############
    elif choice==3:
        while ans=="y" or ans=="Y":
            print("\n\nDELETE CARS!")
            brand=input("\n\nEnter Brand Name: ")
            model=input("Enter Model: ")
            delcar(brand,model)
            ans=input("Would You like to Delete More Cars?(N/Y): ")
############ Find Cars ############
    elif choice==4:
        while ans=="y" or ans=="Y":
            print("\n\nFIND THE PERFECT CAR FOR YOU!")
            print("\n\nHow Do You Want To Find The Car?")
            sort=int(input("\n\n1. Find By Brand Name \n2. Find By Model Name \n3. Find By Engine Type \n4. Find By Number of Seats \n5. Find By Mileage \n6. Find By Maximum Speed \n7. Find By Price \n"))
            if sort==1:
                brand=input("\n\nEnter Your Preferred Brand: ")
                findcarstr("Brand",brand)
            elif sort==2:
                model=input("\n\nEnter The Car Model You Want: ")
                findcarstr("Model",model)
            elif sort==3:
                engine=input("\n\nEnter Your Preferred Engine Type(Petrol/Diesel/CNG/EV): ")
                findcarstr("Engine_Type",engine)
            elif sort==4:
                seat=int(input("\n\nHow Many Seats Do You Want? "))
                findcarint("Seats",seat)
            elif sort==5:
                mileage=int(input("\n\nWhat's Minimum Mileage You Want? "))
                findcarint("Maximum_Mileage",mileage)
            elif sort==6:
                speed=int(input("\n\nHow Fast Do You Want To Drive? "))
                findcarint("Maximum_Speed",speed)
            elif sort==7:
                minprice=int(input("\n\nEnter Minimum Price(in ₹): "))
                maxprice=int(input("\nEnter Minimum Price(in ₹): "))
                carprice(minprice,maxprice)
            else:
                print("\n\nPlease Select from Desired Options!!!")
            ans=input("\n\nWant To Search More Cars?(N/Y) ")
############ Purchase Car ############
    elif choice==5:
        while ans=="y" or ans=="Y":
            print("\n\nBUY YOUR DREAM CAR!")
            invoiceno=int(input("\n\nInvoice Number: "))
            customer=input("Enter Customer Name: ")
            contactno=int(input("Enter Customer Contact No.: "))
            address=input("Enter The Address of Customer: ")
            brand=input("Enter Brand Name: ")
            model=input("Enter Model: ")
            chasis=int(input("Enter Chasis No.: "))
            purchase(invoiceno,customer,contactno,address,brand,model,chasis)
            ans=input("\n\nWant to Purchase More Cars?(N/Y) ")
############ Find A Purchase ############
    elif choice==6:
        while ans=="y" or ans=="Y":
            invoiceno=input("Invoice Number: ")
            with open("Customer.csv","r") as cus:
                tom=csv.reader(cus)
                for i in tom:
                    if i[0]==invoiceno:
                        print("\n\nHere are The Details of the Customer: ")
                        print("Invoice Number: ",i[0])
                        print("Customer Name: ",i[1])
                        print("Contact Number: ",i[2])
                        print("Address: ",i[3])
                        print("Brand: ",i[5])
                        print("Model: ",i[6])
                        print("Chasis Number: ",i[4])
                        print("Total Seats: ",i[7])
                        print("Engine Type: ",i[8])
                        print("Maximum Speed: ",i[9],"km/hr")
                        if i[8]=="EV":
                            print("Maximum Mileage: ",i[10],"km/charge")
                        else:
                            print("Maximum Mileage: ",i[10],"km/l")
                        print("Color: ",i[11])
                        print("Price: ",i[12])
                        print("Payment Mode: ",i[13])
                        break
                else:
                    print("\n\nNo Details Found With Invoice Number: ",invoiceno)
                    print("Please Check The Details and Try Again!!!")
                cus.close()
                ans=input("\n\nWant To Search Details Again?(N/Y) ")
    visit=int(input("\n\nPress 1 To Show Main Menu Options \nPress 2 To Exit\n"))

############ Exit ############
print("\n\n")
print("#################################         Thank You For Visiting Us!         #################################")
print("#################################         Have a Wonderful Day!              #################################")
print("#################################         Hoping You to Visit Again!         #################################")

