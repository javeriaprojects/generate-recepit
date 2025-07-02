
product = input("Enter product name: ")
price = float(input("Enter price (per item): $"))
quantity = int(input("Enter quantity: "))


subtotal = price * quantity
tax_rate = 0.05  
tax = subtotal * tax_rate
total = subtotal + tax

print("\n📄 --- Receipt ---")
print(f"Item: {product}")
print(f"Quantity: {quantity}")
print(f"Price per item: ${price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (5%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("-----------------------")
print("Thank you for shopping!")