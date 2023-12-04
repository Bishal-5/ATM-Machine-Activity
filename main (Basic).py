atm=int(input('Enter Your Card Number: '))
#Checking Data Store
pnb, sbi, axis=10000, 20000, 30000
pnb_atm, sbi_atm, axis_atm=123456, 743503, 100001
pnb_psw, sbi_psw, axis_psw=2000, 2003, 2004

choose=int(input('1. PNB\n2. SBI\n3. AXIS\nChoose Your Bank: '))
#Banking Activity in Looping system
for i in range(30):
    if(choose==1):
        print('........ PUNJAB NATIONAL BANK ATM ........')
        print('1. Deposit\n2. Withdrawl\n3. Check Balance\n4. Exit')
        opt=int(input('What are you doing: '))
        
        if (opt==1 or opt==2 or opt==3):
            pin=int(input('Enter ATM PIN: '))
             #If PIN matched Banking Activity start
             #For activity on pnb account in pnb atm
            if (atm==pnb_atm and pin==pnb_psw):
                if(opt==1):
                    deposit=int(input('Enter Deposit Amount: '))
                    print('Available Balance: /-',pnb+deposit)
                    print('Transction Successful.')
                elif(opt==2):
                    withdrawl=int(input('Enter Withdwawl Amount: '))
                    print('Available Balance: /-',pnb-withdrawl)
                    print('Transction Successful.')
                elif(opt==3):
                    print('Your Current Balance is: /-',pnb)
             #For activity on sbi account in pnb atm
            elif (atm==sbi_atm and pin==sbi_psw):
                if(opt==1):
                    deposit=int(input('Enter Deposit Amount: '))
                    print('Available Balance: /-',sbi+deposit)
                    print('Transction Successful.')
                elif(opt==2):
                    withdrawl=int(input('Enter Withdwawl Amount: '))
                    print('Available Balance: /-',sbi-withdrawl)
                    print('Transction Successful.')
                elif(opt==3):
                    print('Your Current Balance is: /-',sbi)
             #For activity on axis account in pnb atm
            elif (atm==axis_atm and pin==axis_psw):
                if(opt==1):
                    deposit=int(input('Enter Deposit Amount: '))
                    print('Available Balance: /-',axis+deposit)
                    print('Transction Successful.')
                elif(opt==2):
                    withdrawl=int(input('Enter Withdwawl Amount: '))
                    print('Available Balance: /-',axis-withdrawl)
                    print('Transction Successful.')
                elif(opt==3):
                    print('Your Current Balance is: /-',axis)
             #If PIN isn't matched
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
        else:
            print('Alert: Please Select a Valid Activity.')
            
    elif(choose==2):
        print('........ STATE BANK OF INDIA ATM ........')
        print('1. Deposit\n2. Withdrawl\n3. Check Balance\n4. Exit')
        opt=int(input('What are you doing: '))
            
        if (opt==1 or opt==2 or opt==3):
            pin=int(input('Enter ATM PIN: '))
             #If PIN matched Banking Activity start
             #For activity on pnb account in sbi atm
            if (atm==pnb_atm and pin==pnb_psw):
                if(opt==1):
                    deposit=int(input('Enter Deposit Amount: '))
                    print('Available Balance: /-',pnb+deposit)
                    print('Transction Successful.')
                elif(opt==2):
                    withdrawl=int(input('Enter Withdwawl Amount: '))
                    print('Available Balance: /-',pnb-withdrawl)
                    print('Transction Successful.')
                elif(opt==3):
                    print('Your Current Balance is: /-',pnb)
             #For activity on sbi account in sbi atm
            elif (atm==sbi_atm and pin==sbi_psw):
                if(opt==1):
                    deposit=int(input('Enter Deposit Amount: '))
                    print('Available Balance: /-',sbi+deposit)
                    print('Transction Successful.')
                elif(opt==2):
                    withdrawl=int(input('Enter Withdwawl Amount: '))
                    print('Available Balance: /-',sbi-withdrawl)
                    print('Transction Successful.')
                elif(opt==3):
                    print('Your Current Balance is: /-',sbi)
             #For activity on axis account in sbi atm
            elif (atm==axis_atm and pin==axis_psw):
                if(opt==1):
                    deposit=int(input('Enter Deposit Amount: '))
                    print('Available Balance: /-',axis+deposit)
                    print('Transction Successful.')
                elif(opt==2):
                    withdrawl=int(input('Enter Withdwawl Amount: '))
                    print('Available Balance: /-',axis-withdrawl)
                    print('Transction Successful.')
                elif(opt==3):
                    print('Your Current Balance is: /-',axis)
             #If PIN isn't matched
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
        else:
            print('Alert: Please Select a Valid Activity.')
            
    elif(choose==3):
        print('........ AXIS BANK OF INDIA ATM ........')
        print('1. Deposit\n2. Withdrawl\n3. Check Balance\n4. Exit')
        opt=int(input('What are you doing: '))
            
        if (opt==1 or opt==2 or opt==3):
            pin=int(input('Enter ATM PIN: '))
             #If PIN matched Banking Activity start
             #For activity on pnb account in axis atm
            if (atm==pnb_atm and pin==pnb_psw):
                if(opt==1):
                    deposit=int(input('Enter Deposit Amount: '))
                    print('Available Balance: /-',pnb+deposit)
                    print('Transction Successful.')
                elif(opt==2):
                    withdrawl=int(input('Enter Withdwawl Amount: '))
                    print('Available Balance: /-',pnb-withdrawl)
                    print('Transction Successful.')
                elif(opt==3):
                    print('Your Current Balance is: /-',pnb)
             #For activity on sbi account in axis atm
            elif (atm==sbi_atm and pin==sbi_psw):
                if(opt==1):
                    deposit=int(input('Enter Deposit Amount: '))
                    print('Available Balance: /-',sbi+deposit)
                    print('Transction Successful.')
                elif(opt==2):
                    withdrawl=int(input('Enter Withdwawl Amount: '))
                    print('Available Balance: /-',sbi-withdrawl)
                    print('Transction Successful.')
                elif(opt==3):
                    print('Your Current Balance is: /-',sbi)
             #For activity on axis account in axis atm
            elif (atm==axis_atm and pin==axis_psw):
                if(opt==1):
                    deposit=int(input('Enter Deposit Amount: '))
                    print('Available Balance: /-',axis+deposit)
                    print('Transction Successful.')
                elif(opt==2):
                    withdrawl=int(input('Enter Withdwawl Amount: '))
                    print('Available Balance: /-',axis-withdrawl)
                    print('Transction Successful.')
                elif(opt==3):
                    print('Your Current Balance is: /-',axis)
             #If PIN isn't matched
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
        else:
            print('Alert: Please Select a Valid Activity.')   
    else:
        print('Bank Unknown.\nSelect a correct Bank.')