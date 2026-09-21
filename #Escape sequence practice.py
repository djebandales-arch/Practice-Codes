#Student Scholarship Eligibility Checker

#Inputs
import getpass

print("\t\t\t SCHOLARSHIP APPLICATION FORM \t\t\t \n")
name = input("Input your name ---> ")
age = int(input("Input your age ---> "))
is_enrolled = bool(input("Are you currently enrolled? (True or False)"))
gwa = float(input("What is your GWA?"))
monthly_income = float(input("Input your parent's monthly income --> "))
has_award = bool(input("Do you have awards? (True or False)"))
password = getpass.getpass("Please type your password ---> ")

print("=================================================")
#Statements
if age >= 18 and is_enrolled == True:
    print("Accepted: You are eligible.")
    #tier1 gwa
    if gwa <= 1.50:
        basescholarship = 1000
        print("Congratulations, you have,", basescholarship, "base scholarship")
        if monthly_income <= 20000:
            basescholarship += 5000
            print("Congratulations, you have additional base scholarship amount:,", basescholarship)
        else:
            print("Sorry, you are not eligible for the scholarship because you didn't meet the standards")
    elif 1.51 <= gwa <= 2.00:
        basescholarship = 6000
        print("Congratulations, you are eligible. You have,", basescholarship, "amount")
        if has_award == True:
            basescholarship += 1000
            print("Congratulations, you have additional base scholarship amount due to awards:,", basescholarship)
        else: 
            basescholarship = 0
            print("GWA is too high")
    if gwa > 2.00:
        print("GWA is too high")
        if basescholarship > 0:
            print(eval("You have scholarship Adjustment", basescholarship))
    
print("Rejected: Fails baseline eligibility.")
print("\n ==================================================")
print(" Thank you for Applying.")

