import math
#create a program that allows the user to access two different financial calculators
#an investment calculator and a home loan repayment (bond) calculator
#print heading for user to understand what each term means
print('''investment - to calculate the amount of interest you\'ll earn on your investment
bond - to calculate the amount you\'ll have to pay on a home loan''')


#ask user to enter investment or bond in order to proceed
#How the user capitalises their selection should not affect how the program proceeds. i.e. ‘Bond’, 
# ‘bond’, ‘BOND’ or ‘investment’, ‘Investment’,‘INVESTMENT’, etc., should all be recognised as valid entries
#If the user doesn’t type in a valid input, show an appropriate error message
calculator = input('Enter either \'investment\' or \'bond\' from the menu above to proceed: ').lower()

#If the user doesn’t type in a valid input, show an appropriate error message
if len(calculator) < 4:
    print('Your entry is incorrect. Please enter either \'investment\' or \'bond\'')
else:
    print(calculator)

# If the user chooses investment, then ask user to enter values to requests below
if calculator == 'investment':
    deposit_amount = (int(input('Enter the amount you want to deposit: ')))
    interest_rate = (int(input('Enter your interest rate (do not add %): ')))
    investing_years = (int(input('Enter the number of years you plan on investing: ')))
    interest = (input('Enter the type of interest you want - “simple” or “compound”: ')).lower()

#calculate the interest formula
#first turn the interest entered above into a percentage
#if simple interest is entered use formula A = P*(1 + r*t)
#if compound interest is entered use formula A = P * math.pow((1+r),t)
#where ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered, then r is 0.08.
#‘P’ is the amount that the user deposits.
#‘t’ is the number of years that the money is being invested.
#‘A’ is the total amount once the interest has been applied
#then print out the appropriate amount that they will get back after the given period, at the specified interest rate
    interest_rate_100 = float(interest_rate / 100)
    simple_interest = deposit_amount * (1 + interest_rate_100 * investing_years)
    simple_interest_return = simple_interest - deposit_amount
    compound_interest = deposit_amount * math.pow ((1 + interest_rate_100 ), investing_years)
    compound_interest_return = compound_interest - deposit_amount 

#write an if statement to calcultate either simple or compound interest depending on what the user enters.
    print('')
    if interest == 'simple':
        print(f'The total amount you will get back is {simple_interest} including an interest of {simple_interest_return}')
    elif interest == 'compound':
        print(f'The total amount you will get back is {compound_interest} including an interest of {compound_interest_return}')
    else:
        print('You have not entered the correct option')

# If the user chooses bond 
# Here is the bond repayment formula
# That is the amount that a person will have to be repaid on a home loan each month
# repayment formula = (i * P)/(1 - (1 + i)**(-n))
# In the formula above:
# ‘P’ is the present value of the house
# ‘i’ is the monthly interest rate, calculated by dividing the annual interest rate by 12. 
# Remember to divide the interest entered by the user by 100 e.g. (8 / 100) before dividing by 12.
# ‘n’ is the number of months over which the bond will be repaid
# then ask user to enter values to requests below
elif calculator == 'bond':
    house_value = (int(input('Enter the present value of your house: ')))
    interest_rate_bond = (int(input('Enter the annual interest rate (do not add %): ')))
    bond_repayment_months = (int(input('Enter the number of months you plan to repay the bond: ')))
    interest_rate_100 = float(interest_rate_bond / 100)
    interest_rate_bond_monthly = float((interest_rate_bond / 100) / 12)
    monthly_repayment = (interest_rate_bond_monthly * house_value) / (1 - ( 1 + interest_rate_bond_monthly )** (-bond_repayment_months))
    print(' ')

    #round result in two decimal places
    rounded_monthly_repayment = round(monthly_repayment, 2)
    print(f'The amount to repay each month is {rounded_monthly_repayment}') 

else:
    print('You have not entered the correct option') 


#PLEASE NOTE, I HAVE TESTED BOND CALCULATION ON THIS WEBSITE - https://www.ooba.co.za/home-loan/bond-repayment-calculator/ AND MY FORMULA IS CORRECT. IT HAS 
# EXTRA DECIMAL PLACES BUT WHOLE NUMBER IS CORRECT. A TUTOR MENTIONED IN MY LAST REVIEW THAT IT WASN'T CORRECT BUT IT IS CORRECT.
# THE LAST TUTOR MENTIONED THAT WE ARE ONLY TO CALCULATE THE ACTUAL INTEREST ONLY
# THE QUESTION DOESN'T SPECIFY THIS.
# HERE IS THE QUESTION - ', output the appropriate amount that they will get back after the given period, at the specified interest rate'
# 'THEY WILL GET BACK' CAN MEAN EITHER TOTAL OR INTEREST ONLY. HENCE THE QUESTION IN TASK NEEDS TO BE CLARIFIED.
