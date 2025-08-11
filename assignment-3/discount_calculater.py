# PLP
# Week 3
# Assignment 3: Discount calculator program
# Discount calculator program

# Define a function to calculate discounted price
def calculate_discount(price, discount_percent):
    # Check if discount is 20% or more
    if discount_percent >= 20:
        discounted_price = price * (1 - (discount_percent / 100))
        return discounted_price
    else:
        return price

# Prompt the user to input the original price
price = float(input("Input the original price: "))
# Prompt the user to input the discount percentage
discount_percent = float(input("Input the discount percentage: "))

# Call the function with user inputs and store the result
final_price = calculate_discount(price, discount_percent)
# Print the final price after discount
print(final_price)