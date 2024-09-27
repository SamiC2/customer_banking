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
    ## Added code to reprompt user if they enter invalid data types for the input

    savings_balance = float(input("Welcome. Please enter the starting balance for your savings account: "))
    savings_interest = float(input("Now, please enter the interest rate for your savings account: "))
    savings_maturity = int(input("Finally, please enter the number of months you would like to set for your savings account growth: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"\nThe interest you earned for your savings account based on your input was ${interest_earned:,.2f}")
    print(f"Your final savings account balance after accruing interest based on your input was ${updated_savings_balance:,.2f}\n")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("Now let's start with your CD Account. Please enter the starting balance for your CD account: "))
    cd_interest = float(input("Next, please enter the interest rate for your CD account: "))
    cd_maturity = int(input("Finally, please enter the number of months you would like to set for your CD account growth: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"\nThe interest you earned for your CD account based on your input was ${interest_earned:,.2f}")
    print(f"Your final CD account balance after accruing interest based on your input was ${updated_cd_balance:,.2f}\n")

if __name__ == "__main__":
    # Call the main function.
    main()
    print("\nThank you for using our customer banking app. Goodbye!")
