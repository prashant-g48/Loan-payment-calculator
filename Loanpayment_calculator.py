#get details of loan
money_owed=float(input("principal amount of Money you owed\n"))
annual_intrest = int(input("how much yearly intrest rate paid for loan\n"))
monthly_emi_paid=float(input("how much amount is paid monthly\n"))
total_month=input("How many month you want to pay the to complete the loan\n")

Monthly_rate=annual_intrest/100/12

for i in range(int(total_month)):

    #calculate the monthly intrest paid
    intrest_paid= money_owed*Monthly_rate

    #add in intrest
    money_owed=money_owed+intrest_paid

    #payment maid

    money_owed=money_owed-monthly_emi_paid

    if (money_owed - monthly_emi_paid) < 0:
        print("great!!!you have settled your loan in",i+1,"months")
        break

    print("paid",monthly_emi_paid,"with intrest",intrest_paid,end=" ")
    print("now i owe",money_owed)

# a=monthly_emi_paid-intrest_paid
# b=a*12 actual amount paid without intrest
# print("actual amount paid this year",b)
# c=money_owed+b
# print(c)
# d=c-money_owed    calculating actual money paid which should be eqaul to b that should be b=d
# print(d)

