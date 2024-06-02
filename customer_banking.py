# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    print(f"It will be necessary to gather the following information regarding your savings account.")
    savings_balance = float(input("Please enter your savings account balance:"))
    savings_interest = float(input("Please enter the interest rate of your savings account:"))
    savings_maturity = int(input("Please enter the number of months to maturity of your savings account:"))
    print("Thank you for providing your savings account information.")
    
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your interest earned on the savings account is: {savings_interest_earned}")
    print(f"Your savings account balance is: {updated_savings_balance}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    print(f"It will also be necessary to gather the following information regarding your CD account.")
    cd_balance = float(input("Please enter your current cd value:"))
    cd_interest = float(input("Please enter the interest rate of your CD:"))
    cd_maturity = int(input("Please enter the number of months to maturity of your CD:"))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your interest earned on the cd account is: {cd_interest_earned}")
    print(f"Your savings account balance is: {updated_cd_balance}")
    

if __name__ == "__main__":
    # Call the main function.
