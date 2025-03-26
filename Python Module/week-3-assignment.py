# function to calculate the final price after applying discount
def calculate_discount(price, discount_percent):

    if discount_percent >= 20:   # check if the discount percent is greater than or equal to 20
        discount = price * (discount_percent / 100)

# This calculate the final price after applying discount
        final_price = price - discount

        return final_price
    else:
        return price
    
# This function gets the original price and discount percent from the user
def get_final_price():
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percent: "))

        final_price = calculate_discount(price, discount_percent)

        if final_price != price:
            print(f"The final price after applying discount is: ${final_price:.2f}")
        else:
             print(f"The original price is: ${price:.2f} (no discount was applied)")

get_final_price()

