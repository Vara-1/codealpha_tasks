stocks = {"RIL": 180, "TCS": 250, "ICICI": 150}

total = 0

while True:
    name = input("Enter stock name (or 'DONE'): ").upper()
    if name == "DONE":
        break

    qty = int(input("Enter quantity: "))

    if name in stocks:
        total += stocks[name] * qty
    else:
        print("Stock not found")

print("Total Investment:", total)