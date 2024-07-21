#Calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent>= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price-discount_amount
        return final_price
    else:
        return price

# Code to prompt user to enter original price and discount percentage, and then apply the discount using the calculat_discount function
def main():
    original_price = float(input("Enter the original price of the item:"))
    discount_percent = float(input("Enter the discount percentage:"))

    final_price = calculate_discount(original_price,discount_percent)
    print(final_price)

if __name__ == "__main__":
    main()