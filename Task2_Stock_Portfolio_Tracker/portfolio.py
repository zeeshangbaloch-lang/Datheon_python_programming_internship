import csv

# Step 1: dictionary to store all stocks (ticker is the key)
portfolio = {}

print("=== Stock Portfolio Tracker ===")
print("Enter your stocks one by one. Type 'done' as the ticker when finished.\n")

# Step 2: take input for as many stocks as the user wants
while True:
    ticker = input("Enter the ticker symbol (or 'done' to finish): ").strip().upper()
    if ticker == "DONE":
        break
    if ticker == "":
        print("Ticker cannot be empty. Try again.\n")
        continue

    try:
        buy_price = float(input("Enter buy price: "))
        shares = float(input("Enter number of shares: "))
        current_price = float(input("Enter the current price: "))
    except ValueError:
        print("Please enter numbers only. Try this stock again.\n")
        continue

    if buy_price <= 0 or shares <= 0:
        print("Buy price and shares must be greater than 0. Try again.\n")
        continue

    portfolio[ticker] = {
        "buy_price": buy_price,
        "shares": shares,
        "current_price": current_price,
    }
    print(f"Added {ticker}.\n")

if not portfolio:
    print("No stocks entered. Nothing to calculate.")
else:
    # Step 3: calculate for each stock
    rows = []
    total_invested = 0
    total_value = 0

    for ticker, data in portfolio.items():
        invested = data["buy_price"] * data["shares"]
        value = data["current_price"] * data["shares"]
        percent = (value - invested) / invested * 100

        total_invested += invested
        total_value += value

        rows.append([
            ticker,
            data["shares"],
            data["buy_price"],
            data["current_price"],
            round(invested, 2),
            round(value, 2),
            round(percent, 2),
        ])

    total_percent = (total_value - total_invested) / total_invested * 100

    # Step 4: print a formatted summary on the console
    print("\n" + "=" * 78)
    print(f"{'Ticker':<8}{'Shares':>8}{'Buy':>10}{'Now':>10}{'Invested':>12}{'Value':>12}{'Gain/Loss':>12}")
    print("-" * 78)
    for r in rows:
        sign = "+" if r[6] > 0 else ""
        print(f"{r[0]:<8}{r[1]:>8.2f}{r[2]:>10.2f}{r[3]:>10.2f}{r[4]:>12.2f}{r[5]:>12.2f}{sign + format(r[6], '.2f') + '%':>12}")
    print("-" * 78)
    sign = "+" if total_percent > 0 else ""
    print(f"Total invested : {total_invested:.2f}")
    print(f"Total value    : {total_value:.2f}")
    print(f"Overall result : {sign}{total_percent:.2f}%")
    print("=" * 78)

    # Step 5: save the summary to portfolio_summary.csv
    with open("portfolio_summary.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Ticker", "Shares", "Buy Price", "Current Price",
                         "Amount Invested", "Current Value", "Gain/Loss %"])
        writer.writerows(rows)
        writer.writerow(["TOTAL", "", "", "", round(total_invested, 2),
                         round(total_value, 2), round(total_percent, 2)])

    print("\nSaved results to portfolio_summary.csv")
