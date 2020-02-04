import os
import sys
print("\n\t  ::: Create Files With Password And Open Those ::: \n")
def intro():
    print(" 1. New Member? Create An Account")
    print(" 2. Log in")
    print(" 3. Exit")
    introInput=int(input("\n Enter 1 or 2 or 3 : "))
    while(introInput!=1 and introInput!=2 and introInput!=3):
        print(" Oops!!! Please Enter 1 Or 2 or 3!!!")
        introInput=int(input("\n Enter 1 or 2 or 3 : "))
    return introInput

def isLowerCase(s):
    for i in range(0,len(s)):
        if ord(s[i])<97 or ord(s[i])>122:
            return False
    return True

input1=intro()
while input1!=3:
    if input1==1:
        newMemberUserName=input("\n Enter A User Name (Contains Only Lower Case Latters): ")
        checkPoint=isLowerCase(newMemberUserName)
        while not checkPoint:
            print(" User Name Should Be In Lower Case!!!")
            newMemberUserName=input("\n Enter A User Name (Contains Only Lower Case Latter): ")
            checkPoint=isLowerCase(newMemberUserName)
        while os.path.exists(newMemberUserName+".txt"):
            print(" Sorry!!! The User Name Already Taken")
            print(" Please Try Again")
            newMemberUserName=input(" Enter A User Name : ")
        newMemberPassword=input(" Enter A Password : ")
        newMemberFile=open(newMemberUserName+".txt","w+")
        newMemberFile.write("PassWord : "+newMemberPassword)
        newMemberFile.close()
        print(" Congratulations!!! Your File Has Been Made Successfully In Same Directry!!!")

    elif input1==2:
        memberUserName=input("\n Enter User Id : ")
        while not os.path.exists(memberUserName+".txt"):
            print(" Sorry!!! User Id Doesn't Match!!!")
            print(" Please Try Again")
            memberUserName=input(" Enter User Id : ")
        realFile=open(memberUserName+".txt","r")
        if realFile.mode=="r":
            contents=realFile.read()
            checkableString=contents
        realFile.close()
        memberPassword=input(" Enter Password : ")
        while "PassWord : "+memberPassword!=checkableString:
            print(" Sorry!!! The Password Doesn't Match!!!")
            print(" Please Try Again")
            memberPassword=input(" Enter Password : ")
        print(" You Successfully Log In")

    input1=intro()
print("\n See You Soon!!!")
sys.exit(0)
