#Pythton Program To Generate and Save Passwords

print("______________________________________________________________________________________________________________________________")
print()
print("                                                 PassGen Password Generator                                                   ")
print()
print("Created By: KARAN GHARDE")
print("GitHub Link: https://github.com/karan13-collab/")
print("Instagram: @mrlucrative13")
print("Twitter: @MrLucrative13")
print("Subscribe To My YouTube Channel: MrLucrative")
print("Channel Link: https://www.youtube.com/channel/UCz1eCHc87azq16TSr-50Bcg")
print("Read Documentation before using the program.")
print()
print()
print("______________________________________________________________________________________________________________________________")
print()
print()

#########################################################################################################################################

#                                                         Main Program Starts Here!                                                    #

#########################################################################################################################################

import random
import pickle
isTrue=True
while isTrue==True:
    choice=int(input("1. Generate Password \n2. View Passwords  \n3. Change Password of Password File \n4. Exit\n\n"))
    if choice==1:
        l1=[]
        for i in range(0,8):
            r=random.randint(0,9)
            l1.append(str(r))
        l2=[]
        for i in range(0,6):
            a=random.randint(65,90)
            A=chr(a)
            l2.append(A)
        l3=[]
        for i in range(0,6):
            b=random.randint(97,122)
            B=chr(b)
            l3.append(B)
        s=['@','#','$','%','&','*','-','+','/','(',')']
        S=[]
        for i in range(0,5):
            t=random.choice(s)
            S.append(t)
        l1.extend(l2)
        l1.extend(l3)
        l1.extend(S)
        L=set(l1)
        st=''
        print("The Generated Password is: ",end='')
        for i in L:
            st=st+i
        print(st)
        t=int(input("Want to save password? \n1. Yes \n2. No     "))
        if t==1:
            Web=input("Website/App Name: ")
            Us=input("EMail/Username/Phone: ")
            save={"Website":Web.lower(),"User":Us,"Password":st}
            f=open("PassGen.dat",'ab')
            pickle.dump(save,f)
        elif t==2:
            break
    elif choice==2:
        found=0
        passwd=input("Enter Password: ")
        f=open("Pass.dat",'rb')
        try:
            while True:
                pss=pickle.load(f)
        except EOFError:
            f.close()
        if passwd==pss:
            f=open("PassGen.dat",'rb')
            chuce=int(input("\n1. Display Password Corresponding to a Website \n2. Display all Passwords \n3. Main Menu \n\n"))
            if chuce==1:
                Web=input("Enter Website: ")
                try:
                    while True:
                        i=pickle.load(f)
                        if i["Website"]==Web.lower():
                            print("Here are The Details: ")
                            print("Website: ",i["Website"])
                            print("User: ",i["User"])
                            print("Password: ",i["Password"])
                            print("\n\n\n\n")
                            found=1
                except EOFError:
                    f.close()
                if found==0:
                    print("Sorry! No Record Found!")
            elif chuce==2:
                try:
                    while True:
                        i=pickle.load(f)
                        print("Here are The Details: ")
                        print("Website: ",i["Website"])
                        print("User: ",i["User"])
                        print("Password: ",i["Password"])
                        print("\n")
                except EOFError:
                    f.close()
            elif chuce==3:
                break
            else:
                print("Please Choose Valid Option!\n")
        else:
            print("Wrong Password!\n\n")
            
        
    elif choice==3:
        oldp=input("Old Password: ")
        f=open("Pass.dat",'rb')
        try:
            while True:
                old=pickle.load(f)
        except EOFError:
            f.close()
        if oldp==old:
            new=input("New Password: ")
            f=open("Pass.dat",'wb')
            pickle.dump(new,f)
            print("\nPassword Changed Successfully!")
            f.close()
        else:
            while True:
                print("\n\n##########    Wrong Password    ##########")
                choice1=int(input("\n1. Try Again \n2. Main Menu  \n"))
                if choice1==1:
                    true=True
                    break
                elif choice2==2:
                    true=False
                    break
                else:
                    print("Please Enter Valid Option!")
    elif choice==4:
        print("Thank You For Using PassGen Password Generator!")
        break
    else:
        print("Please Choose Valid Option")
