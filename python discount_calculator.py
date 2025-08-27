def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is less than 20%, no discount is applied.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price


# Main program
try:
    # Prompt user for input
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(price, discount_percent)

    # Output result
    if discount_percent >= 20:
        print(f"The final price after {discount_percent}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: {final_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")
