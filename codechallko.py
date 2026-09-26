#Mobile Phone Plan Eligibility & Bill Calculator

customer_name = input("What is your name? --> ")
age = int(input("What is your age? --> "))
is_employed = bool(input("Are you currrently employed --> ")== "Yes" or "yes")
credit_score = int(input("What is your Credit Score --> "))
monthly_income = float(input("What is your monthly income --> "))
has_autopay = bool(input("Do you have autopay? -->")== "True" or "yes")
data_gb = float(input("Input your data GB --> "))
import getpass
password = getpass.getpass("Type your password --> ")

base_bill = 0.0
additional = 0.0
compute = 0.0
risk_charge = 0.0

if age >= 18 and is_employed == True:
    print("You are eligible for a postpaid plan.")
    if credit_score >= 750:
        base_bill += 1200
        print("Your base bill is", base_bill)
        if monthly_income >= 30000:
            compute = base_bill/10 
            additional = base_bill - compute 
            print("Your base bill is reduced by 10 Percent, so your base bill is now", additional)
    if data_gb > 20:
        additional += 200
    elif data_gb <= 5:
        additional -= 100
    if 600 <= credit_score < 750 and has_autopay == True:
        base_bill = 1000
        additional = base_bill - 100
        print("Your total base bill is", additional)
    if 600 <= credit_score < 750 and has_autopay == True and monthly_income < 20000:
            base_bill = 1000
            additional = base_bill - 100
            risk_charge = additional + 150
            print("But since you didn't meet the monthly income criteria, we added 150 for risk charge. Your total base bill is", risk_charge)
    elif credit_score < 600:
         print("Rejected: Credit Score too low.")
    if data_gb > 20:
        additional += 200
    elif data_gb <= 5:
        additional -= 100
else:
    print("Rejected: Fails baseline criteria")
