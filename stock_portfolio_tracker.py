STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320,
}

print("Stock names are based on the companies. Please enter stock names in uppercase.")
print("Available stocks: AAPL, TSLA, GOOGL, AMZN, MSFT\n")


def get_user_portfolio():
    portfolio = {}

    while True:
        stock_name = input("Enter stock name (or 'done' to finish): ").strip().upper()

        if stock_name == "DONE":
            break

        if stock_name not in STOCK_PRICES:
            print("Stock not found. Please enter a valid stock name.")
            continue

        quantity_text = input("Enter quantity: ").strip()

        if not quantity_text.isdigit() or int(quantity_text) <= 0:
            print("Please enter a valid positive number for quantity.")
            continue

        quantity = int(quantity_text)

        if stock_name in portfolio:
            portfolio[stock_name] += quantity
        else:
            portfolio[stock_name] = quantity

    return portfolio


def calculate_portfolio_value(portfolio):
    portfolio_details = []
    total_value = 0

    for stock_name, quantity in portfolio.items():
        price = STOCK_PRICES[stock_name]
        investment_value = price * quantity
        portfolio_details.append((stock_name, quantity, price, investment_value))
        total_value += investment_value

    return portfolio_details, total_value


def display_portfolio(portfolio_details, total_value):
    print("\nPortfolio Summary")
    print("-----------------")

    for stock_name, quantity, price, investment_value in portfolio_details:
        print(f"{stock_name} : {quantity} shares x ${price} = ${investment_value}")

    print(f"\nTotal Investment Value: ${total_value}")


def save_portfolio_to_file(portfolio_details, total_value):
    with open("portfolio_summary.txt", "w") as file:
        file.write("Portfolio Summary\n")
        file.write("-----------------\n")

        for stock_name, quantity, price, investment_value in portfolio_details:
            file.write(f"{stock_name} : {quantity} shares x ${price} = ${investment_value}\n")

        file.write(f"\nTotal Investment Value: ${total_value}\n")


def main():
    portfolio = get_user_portfolio()
    portfolio_details, total_value = calculate_portfolio_value(portfolio)
    display_portfolio(portfolio_details, total_value)
    save_portfolio_to_file(portfolio_details, total_value)


if __name__ == "__main__":
    main()

