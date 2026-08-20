stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 185,
    "MSFT": 420
}

portfolio = {}

print("Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input(
        "\nEnter stock symbol, or type 'done' to finish: "
    ).upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be positive.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    except ValueError:
        print("Please enter a valid whole number.")

total_value = 0

print("\nPortfolio Summary")
print("-" * 35)

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value

    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print("-" * 35)
print(f"Total investment value: ${total_value}")

save_file = input(
    "\nSave the result to portfolio.txt? (yes/no): "
).lower().strip()

if save_file == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Portfolio Summary\n")
        file.write("-" * 35 + "\n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity

            file.write(
                f"{stock}: {quantity} shares = ${value}\n"
            )

        file.write("-" * 35 + "\n")
        file.write(
            f"Total investment value: ${total_value}\n"
        )

    print("Portfolio saved to portfolio.txt.")
