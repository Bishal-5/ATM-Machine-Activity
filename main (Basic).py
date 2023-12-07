# All Data Store Here
pnb, sbi, axis=10000, 20000, 30000
pnb_atm, sbi_atm, axis_atm=123456, 743503, 100001
pnb_ac, sbi_ac, axis_ac=9836897111, 6289869613, 0000000000
pnb_pin, sbi_pin, axis_pin=2000, 2003, 2004
pnb_cvv, sbi_cvv, axis_cvv=200, 300, 400

# ATM Choosing
def atm_choose():
    choose_atm=int(input('1. PNB ATM\n2. SBI ATM\n3. AXIS ATM\nChoose Your ATM: '))
    if choose_atm==1:
        print('----- PNB ATM -----')
    elif choose_atm==2:
        print('----- SBI ATM -----')
    else:
        print('----- AXIS ATM -----')
    
# Wishing Message to User
import datetime as dt
time=dt.datetime.now()
hour=time.hour
print("Current Time:",time.strftime("%X"))
if hour>6 and hour<12:
    print('... Good Morning! ...')
elif hour>12 and hour<18:
    print('... Good Afternoon! ...')
elif hour>18 and hour<22:
    print('... Good Evening! ...')
else:
    print('... Good Night! ...')

# Banking Activity Start
atm_choose()
atm=int(input('Enter Your Card Number: '))
choose=int(input('1. PNB Bank\n2. SBI Bank\n3. AXIS Bank\nChoose Your Bank: '))
for i in range(30):
     # Activity in PNB Bank
    if(choose==1):
        print('........ PUNJAB NATIONAL BANK ........')
        print('1. Deposit\n2. Withdrawl\n3. Check Balance\n4. Exit')
        opt=int(input('What are you like to do: '))
         # Deposit
        if (opt==1):
            ac_no=int(input('Enter Your Account Number: '))
            deposit=int(input('Enter Deposit Amount: '))
            print('Transction Successful.')
            print('Available Balance: /-',pnb+deposit)
         # Withdwawl 
        elif (opt==2 or opt==3):
            pin=int(input('Enter Your ATM PIN: '))
            if (pin == pnb_pin):
                if(opt==2):
                    cvv=int(input('Enter CVV: '))
                    if cvv==pnb_cvv:
                        withdrawl=int(input('Enter Withdwawl Amount: '))
                        if (pnb>=withdrawl):
                            print('Transction Successful.')
                            print('Available Balance: /-',pnb-withdrawl)
                        else:
                            print('Insufficient Balance.')
                            break
                    else:
                        print('Alert: You Entered Wrong CVV.')
                 # Balance Check
                elif(opt==3):
                    print('Your Current Balance is: /-',pnb)
             # Transction Canceling for giving wrong pin
            else:
                print('Alert: Please Enter Correct ATM No. or PIN.')
                if i==0:
                    print('You Have Only Two Times to Enter Correct PIN.')
                elif i==1:
                    print('You Have Only One Times to Enter Correct PIN.')
                elif i==2:
                    print('You Entered Many Wrong Attempts.\nTransction Cancel. Try Again.')
                    break
        elif (opt==4):
            print('******** Thank You. Visit Again ********')
            break
        
     #Activity in SBI Bank
    elif (choose==2):
        print('........ STATE BANK OF INDIA ........')
        print('1. Deposit\n2. Withdrawl\n3. Check Balance\n4. Exit')
        opt=int(input('What are you like to do: '))
         # Deposit
        if (opt==1):
            ac_no=int(input('Enter Your Account Number: '))
            deposit=int(input('Enter Deposit Amount: '))
            print('Transction Successful.')
            print('Available Balance: /-',sbi+deposit)
         # Withdrawl
        elif (opt==2 or opt==3):
            pin=int(input('Enter Your ATM PIN: '))
            if (pin == sbi_pin):
                if(opt==2):
                    cvv=int(input('Enter CVV: '))
                    if cvv==sbi_cvv:
                        withdrawl=int(input('Enter Withdwawl Amount: '))
                        if (pnb>=withdrawl):
                            print('Transction Successful.')
                            print('Available Balance: /-',sbi-withdrawl)
                        else:
                            print('Insufficient Balance.')
                            break
                    else:
                        print('Alert: You Entered Wrong CVV.')
                 # Balance Check
                elif(opt==3):
                    print('Your Current Balance is: /-',sbi)
             # Transction Canceling for giving wrong pin
            else:
                print('Alert: Please Enter Correct ATM No. or PIN.')
                if i==0:
                    print('You Have Only Two Times to Enter Correct PIN.')
                elif i==1:
                    print('You Have Only One Times to Enter Correct PIN.')
                elif i==2:
                    print('You Entered Many Wrong Attempts.\nTransction Cancel. Try Again.')
                    break
        elif (opt==4):
            print('******** Thank You. Visit Again ********')
            break
        
     #Activity in AXIS Bank
    elif (choose==3):
        print('........ AXIS BANK OF INDIA ........')
        print('1. Deposit\n2. Withdrawl\n3. Check Balance\n4. Exit')
        opt=int(input('What are you like to do: '))
         # Deposit
        if (opt==1):
            ac_no=int(input('Enter Your Account Number: '))
            deposit=int(input('Enter Deposit Amount: '))
            print('Transction Successful.')
            print('Available Balance: /-',axis+deposit)
         # Withdrawl
        elif (opt==2 or opt==3):
            pin=int(input('Enter Your ATM PIN: '))
            if (pin == sbi_pin):
                if(opt==2):
                    cvv=int(input('Enter CVV: '))
                    if cvv==axis_cvv:
                        withdrawl=int(input('Enter Withdwawl Amount: '))
                        if (axis>=withdrawl):
                            print('Transction Successful.')
                            print('Available Balance: /-',axis-withdrawl)
                        else:
                            print('Insufficient Balance.')
                            break
                    else:
                        print('Alert: You Entered Wrong CVV.')
                 # Balance Check
                elif(opt==3):
                    print('Your Current Balance is: /-',axis)
             # Transction Canceling for giving wrong pin
            else:
                print('Alert: Please Enter Correct ATM No. or PIN.')
                if i==0:
                    print('You Have Only Two Times to Enter Correct PIN.')
                elif i==1:
                    print('You Have Only One Times to Enter Correct PIN.')
                elif i==2:
                    print('You Entered Many Wrong Attempts.\nTransction Cancel. Try Again.')
                    break
        elif (opt==4):
            print('******** Thank You. Visit Again ********')
            break
