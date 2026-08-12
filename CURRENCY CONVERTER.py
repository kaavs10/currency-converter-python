
print("      CURRENCY COVNVERTER         ")

print("\nAvailable Currencies")
print("1. INR (Indian Rupee)")
print("2. USD (US Dollar)")
print("3. EUR (Euro)")
print("4. GBP (British Pound)")
print("5. JPY (Japanese Yen)")

rates = {
    "INR": 1,
    "USD": 96.50,
    "EUR": 109,
    "GBP": 129,
    "JPY": 0.59
}

from_currency = input("\nConvert FROM (INR/USD/EUR/GBP/JPY): ").upper()
to_currency = input("Convert TO (INR/USD/EUR/GBP/JPY): ").upper()

if from_currency not in rates or to_currency not in rates:
    print("\n Invalid currency entered.")
else:
    amount = float(input("Enter amount: "))

    # Convert to INR first
    amount_in_inr = amount * rates[from_currency]

    # Convert INR to desired currency
    converted_amount = amount_in_inr / rates[to_currency]


    print("      CONVERSION RESULT")
    print(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

print("\nThank you for using the Currency Converter!")

