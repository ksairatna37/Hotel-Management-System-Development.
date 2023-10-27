
from termcolor import colored
from audioop import add
from glob import glob
import string
from traceback import print_tb
import numpy as np
import random
import datetime
from datetime import timedelta
import os
import pandas as pa



def packages():
    text = colored('2nd, 3rd and 4th floors', 'red')
  
    print("""
Packages that We Offer
        1.Luxury Room
          These cozy windowless rooms located in the historic Palace Wing offer you complete tranquillity.""")
            
    print("\n\t2.Luxury Grande Room City View")
    print("\tThese rooms are located in the Palace Wing on the "+text+".") 
    
    print(""" 
            
        3.Luxury Grande Room Sea View
          These rooms offer spectacular views of the Arabian Sea or the Gateway of India.
            
        4.The Tata Suite
          Created in the honor of our Founder with extravagance of lush carpets and fine architectural detailing.
            
            (Note - All Packages include Complimentary Wifi Service ,King size bed can accomodate upto 3 guests.)
          """)
    text101=colored('Press Enter\n','blue')
    g=input(text101)
  
    print("""
              (Note - Starting Rate/Night)
              
              1.Luxury Room                      Rs.4000*
              2.Luxury Grande Room City View     Rs.7000*
              3.Luxury Grande Room Sea View      Rs.10000*
              4.The Tata Suite                   Rs.15000*
              """)
    selectpackage()
    
        
def selectpackage():
    print("Please select package")
    global select
    select=int(input())
    print("For how many nights you are willing to stay")
    global night
    night=int(input())
    global packagename
    if select ==1:
        packagename="Luxury Room"
        arr=np.array([101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120])
        arr1=(np.random.choice(arr,size=3,replace=False))   
        a=arr1 
    elif select ==2:
        packagename="Luxury Grande Room City View"
        arr=np.array([201,203,205,207,208,209,210,212,213,214,223,312,354,316,359,333,327,369,330,342,360,364,421,456,412,489,423,410,412,432,465,474,416])
        arr2=(np.random.choice(arr,size=3,replace=False))
        a=arr2
    elif select ==3:
        packagename="Luxury Grande Room Sea View"
        arr=np.array([706,704,752,746,712,795,734,761,792,749,768,713,741])
        arr3=(np.random.choice(arr,size=3,replace=False))
        a=arr3
    elif select ==4:
        packagename="The Tata Suite"
        arr=np.array([906,904,952,946,912,995,934,961,992,949,968,913,941])
        arr4=(np.random.choice(arr,size=3,replace=False))
        a=arr4
    
    print("\nWe have These Three rooms available right now,please select one:")
    
    global roomnumber
    roomnumber= 3

    while roomnumber not in a:
        print(a)
        
        roomnumber=int(input())

        if roomnumber not in a:
            text1=colored('Wrong Roomnumber !', 'red')
  
            print(text1+" !,This room is aready booked by someone else please select correct one")
        

    

    global roomrent
    if select==1:
       roomrent=4000*night
    elif select==2:
        roomrent=7000*night
    elif select==3:
        roomrent=10000*night
    elif select==4:
        roomrent=15000*night
    
    
    
def customerinfo():
    text2=colored('\nEnter Customer Details:', 'green')
    print(text2)
    print("Customer Name")
    global name
    name=input()
    print("Customer email id")
    global email
    email=input()
    print("Customer phone number")
    global phone
    phone=input()
    print("Customer's address")
    global address
    address=input()
    os.system('cls')
    
def checkcustomer():
    os.system('cls')
    text3=colored('\nCustomer Details:', 'blue')
    print(text3)
    print("Customer Name :",name)
    print("Customer email id :",email)
    print("Customer phone number :",phone)
    print("Customer's address :",address)
    
    

def checkroom():
    os.system('cls')
    text4=colored('\nRoom Details:', 'blue')
    print(text4)
    print("Package Name :",packagename)
    print("Room Number :",roomnumber)
    print("Room Rent :",roomrent)
    
    
def makepayment(val):
    global grand
    global bill
    global sum2
    global sum3
    global key
    global zzz
    global ppp
    global kkk
    global lll
    if val==1:
        if key==1:
            zzz=1
            print("Your Total Room bill is ",grand)
            key=key+1
            defpay()
        elif key!=1:
            text106=colored('You have already paid bill !','red')
            print(text106)
            
    elif val==2:
        ppp=1
        print("Your Total Food Bill is ",bill)
        defpay()
    elif val==3:
        kkk=1
        print("Your Total Gamimg bill is ",sum2)
        defpay()
    elif val==4:
        lll=1
        print("Your Total laundry bill is ",sum3)
        defpay()
        
def defpay():
    print("\nPlease select payment mode:")
    print("\t1.Pay by cash")
    print("\t2.Pay Online")
    b=int(input())
    global flag
    if b==1:
        flag=5
        print("")
    elif b==2:
        print("\n\t1.Credit/Debit Card")
        print("\t2.UPI")
        print("\t3.Scan The QR Code")
        
        print("\nPlease select payment options:")
        d=int(input())
        
        flag=1
        if d==1:
            flag=2
            print("Enter 16 digit Card Number")
            cardnumber=input()
            print("Expiry Date :(MM/YY)")
            expirydate=input()
            print("enter 3 digit CVV :")
            cvv=input()
        elif d==2:
            flag=3
            print("please enter UPI ID")
            UPI =input()
        elif d==3:
            flag=4
            print("please scan the QR code")
        
    print("\nIf payment done press 1")
    c=int(input())
    if c==1:
        print("Thank you for payment")
    else:
        print("You have to make payment to buy a room")
    
    
    
def food():
    os.system('cls')
    text7=colored('ORDER YOUR FOOD:','green')
    print("\n"+text7)
    dc = input('YOU WANT DRINK ? YES OR NO\n')
    global bill
    bill=0
    nbill=0
    ms=0
    sum=0
    sum1=0
    if dc == "YES":
        text8=colored('---------------- DRINKS -----------------','yellow')
        print(text8)
        print("""    
      1)Cola          20rs
      2)Nestea        30rs
      3)Sprite        40rs
      4)Mojito        60rs
      5)Gin tonic     60rs
      6)Whiskey       300rs
            """)
        
        z="YES"
        while(z=="YES"):
            w = int(input("ENTER YOUR CHOISE NO"))
            
            q = int(input("quantity"))
            if w == 1:
                nbill = 20*q
            elif w == 2:
                nbill = 30*q
            elif w == 3:
                nbill = 40*q
            elif w == 4:
                nbill = 60*q
            elif w == 5:
                nbill = 60*q
            elif w == 6:
             nbill = 300*q
             
            sum1=sum1+nbill
             
            print("do you want to buy more")
            z=input()

    mc = input('YOU WANT MAIN COURSE ? YES OR NO\n')
    if mc=="YES":
        text9=colored('---------------- MAIN COURSE -----------------','yellow')
        print(text9)
        print("""
      1)PANEER             300rs
      2)KAJU CURRY         300rs
      3)PANNER MASALA      350rs
      4)KAJU MASALA        350rs
      5)PASTA              300rs
      6)MALAI KOFTA        400rs
      7)VEG PARATHA        350rs      
        """)
        y="YES"
        while (y=="YES"):
            e = int(input("ENTER YOUR CHOISE NO"))
            d =int(input("quantity"))
            if e==1:
                ms = 300*d
            elif e==2:
                ms = 300 * d
            elif e == 3:
             ms = 350 * d
            elif e==4:
                ms = 350 * d
            elif e==5:
                ms = 300 * d
            elif e==6:
                ms = 400 * d
            elif e==7:
                ms = 350 * d
              
            sum=sum+ms
            
            print("do you want to buy more")
            y=input()
            
    
    bill=sum+sum1
    text26=colored(bill,'green')
    print("\n\t\t\tFood bill :",text26)
    
    global totalbill
    totalbill=totalbill+bill
    text27=colored(totalbill,'green')
    print("\n\t\t\tTotal Food bill :",text27)
    os.system("PAUSE")
    
def calall():
    global grand
    global roomrent
    grand=roomrent+800


def receipt():
    global zzz
    global ppp
    global kkk
    global lll
    text18=colored('-------------------- BILL RECEIPT ----------------------','blue')
    print(text18)
    print("--------------------------------------------------------")
    text10=colored('Branch','yellow')
    print(text10+" : Mumbai")
    x=datetime.datetime.now()
    text11=colored('Check In Date:','yellow')
    print(text11+"\t",x.strftime("%c"))
    y=x+timedelta(days=(night+1))
    text12=colored('Check Out Date:','yellow')
    print(text12+"\t",y.strftime("%c"))
    text13=colored('Customer Details','yellow')
    print(text13)
    print("--------------------------------------------------------")
    print("Customer Name:\t\t\t\t\t",name)
    print("Customer Email ID:\t\t\t\t",email)
    print("Customer Phone Number:\t\t\t\t",phone)
    print("Customer Address:\t\t\t\t",address)
    print("--------------------------------------------------------")
    print("Package Name :",packagename)
    print("Room Number :",roomnumber)
    print("--------------------------------------------------------")
    text14=colored('Services','yellow')
    text15=colored('Cost','yellow')
    print(text14+"\t\t\t\t"+"  "+text15)
    if zzz==1:
        print("Room Rent\t\t\t\t"+"Rs.",roomrent," ✅")
    else:
        print("Room Rent\t\t\t\t"+"Rs.",roomrent)
    
    if ppp==1:
        print("Food Bill\t\t\t\t"+"Rs.",totalbill," ✅")
    else:
        print("Food Bill\t\t\t\t"+"Rs.",totalbill) 
    
    if kkk==1:
        print("Gaming Bill\t\t\t\t"+"Rs.",totalgamebill," ✅")
    else:
        print("Gaming Bill\t\t\t\t"+"Rs.",totalgamebill)
    
    if lll==1:    
        print("Laundry Bill\t\t\t\t"+"Rs.",totallaundry," ✅")
    else:
        print("Laundry Bill\t\t\t\t"+"Rs.",totallaundry)
        
        
    print("--------------------------------------------------------")
    roomservice=800
    subtotal=roomrent+bill+sum2+sum3
    print("\nSub Total Bill\t\t\t\tRs.",subtotal)
    print("Additional Service Charges\t\tRs.",roomservice)
    print("--------------------------------------------------------")
    global grand
    grand=subtotal+roomservice
    global text16
    text16=colored(grand,'green')
    print("Grand Total Bill\t\t\tRs.",text16)
    print("--------------------------------------------------------")
    global roombill
    roombill=roomrent+800
    global ki
    
    
    text98=colored('Payment done through','blue')
    print(text98)
    if flag==1:
        print("\n-")
    elif flag==2:
        print("Credit/Debit Card")
    elif flag==3:
        print("UPI ID")
    elif flag==4:
        print("QR Code")
    elif flag==5:
        print("Cash")
    
    

    




    
def game():
        os.system('cls')
        global mk
        mk=0
        global sum2
        sum2=0
        text23=colored('--------------------  GAME PARLOUR   -----------------------')
        print(text23)
        print ("""
            (Prices mentioned as per hour)\n
            1.Table tennis          Rs.120
            2.Swimming              Rs.170
            3.Bowling               Rs.200
            4.Snooker               Rs.120
            5.Video games           Rs.100
            6.Pool                  Rs.150
            7.Exit""")
    
        while (1):

            
            g=int(input("Enter your choice:"))


            if (g==1):
                h=int(input("No. of hours:"))
                mk=120*h

            elif (g==2):
                h=int(input("No. of hours:"))
                mk=170*h

            elif (g==3):
                h=int(input("No. of hours:"))
                mk=200*h

            elif (g==4):
                h=int(input("No. of hours:"))
                mk=120*h

            elif (g==5):
                h=int(input("No. of hours:"))
                mk=100*h
            elif (g==6):
                h=int(input("No. of hours:"))
                mk=150*h
            elif (g==7):
                break;

            else:

                print ("Invalid option")
                
            sum2=sum2+mk
            
            text20=colored(sum2,'green')
        print ("""
                Gaming Cost           Rs""",text20,"\n")
        
        global totalgamebill
        totalgamebill=totalgamebill+sum2
        
        text30=colored(totalgamebill,'green')
        print ("""
               Total Gaming Cost           Rs""",text30,"\n")
        os.system("PAUSE")
    
def query():
    os.system('cls')
    print("If You have Any Query Regarding Bill receipt or hotel management ,feel free to contact\n")
    
    j=pa.read_csv('Book1.csv')
    print(j.to_string())
    os.system("PAUSE")
        
        
def laundry():
    os.system('cls')
    global sk
    sk=0
    global sum3
    sum3=0
    
    print("""
            --------------------  LAUNDRY MENU   -----------------------
         """)

    print ("""
               1.Shorts                 Rs.10
               2.Trousers               Rs.15
               3.Shirt                  Rs.20
               4.T-Shirt                Rs.15
               5.Jeans                  Rs.20
               6.Saari                  Rs.20
               7.Skirts and dresses     Rs.15
               8.Exit""")

    while (1):

            e=int(input("Enter your choice:"))

            if (e==1):
                f=int(input("Enter the quantity:"))
                sk=10*f

            elif (e==2):
                f=int(input("Enter the quantity:"))
                sk=15*f

            elif (e==3):
                f=int(input("Enter the quantity:"))
                sk=20*f

            elif (e==4):
                f=int(input("Enter the quantity:"))
                sk=15*f

            elif (e==5):
                f=int(input("Enter the quantity:"))
                sk=20*f
            elif (e==6):
                f=int(input("Enter the quantity:"))
                sk=20*f
            elif (e==7):
                f=int(input("Enter the quantity:"))
                sk=15*f
            elif (e==8):
                break;
            else:

                print ("Invalid option")
                
            sum3=sum3+sk
            text21=colored(sum3,'green')
    print(""" Laundary Cost           Rs""",text21,"\n")
    
    global totallaundry
    totallaundry=totallaundry+sum3
    text31=colored(totallaundry,'green')
    print("""Total Laundary Cost           Rs""",text31,"\n")
    os.system("PAUSE")
        
def main():
    os.system('cls')
    global bill
    bill=0
    global sum2
    sum2=0
    global sum3
    sum3=0
    global flag
    flag=0
    global totalbill
    totalbill=0
    global totalgamebill
    totalgamebill=0
    global totallaundry
    totallaundry=0
    global grand
    grand=0
    global roombill
    roombill=0
    global key
    key=1
    global ki
    ki=2
    global zzz
    zzz=2
    global ppp
    ppp=2
    global lll
    lll=2
    global kkk
    kkk=2
    text6=colored('WELCOME TO GALAXY HOTEL, MUMBAI','yellow')
    print ("""
        --------------------------------------------------------------""")
    print("\n\t-------------- "+text6+" ---------------");
    print("""
        --------------------------------------------------------------
        """)
     
    packages()
    customerinfo()
    calall()
    print("--------------",roomrent)
    o="1"
    while o!=9:
        print("\n1.Check Customer Details")
        print("2.Check Room Details")
        print("3.Food Menu")
        print("4.Game Parlour")
        print("5.Laundry")
        print("6.Regarding Query")
        print("7.Bill Receipt")
        print("8.Make Payment")
        print("9.Exit")
        text23=colored("Select Services",'blue')
        print("\n"+text23)
        o=int(input())
       
        if o==1:
            checkcustomer()
            print("\n")
        elif o==2:
            checkroom()
            print("\n")
        elif o==3:
            flag=0
            food()
            print("\n")
        elif o==4:
            game()
            print("\n")
        elif o==5:
            laundry()
            print("\n")
        elif o==6:
            query()
            print("\n")
        elif o==7:
            receipt()
            print("\n")
        elif o==8:
            print("1.Room payment\n2.Food court Payment\n3.Gaming Payment\n4.Laundry Payment\n\nSelect choice")
            choice=int(input())
            makepayment(choice)
            print("\n")
        elif o==9:
            break
            

    print("Please Give Us Feedback , press 1 for yes or 0 for no")
    feed=int(input())
    if feed==1:
        print("Feedback :")
        feedback=input()
        print("Thank You For Choosing Our Services")
    elif feed==0:
        print("Thank You For Choosing Our Services")
main()