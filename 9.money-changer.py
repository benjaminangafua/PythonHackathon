"""
Money Changer

TODO: Write a program that prompts users for an amount and the currency they want to change to.

The program should print out the amount in the currency the entered.

Let's assume currencies are only LRD/USD or lrd/usd.

Example 1:

Amount: 5
Currency: USD
750 LRD

Example 2:

Amount: 750
Currency: lrd
5 USD
"""

def main():
    amount = int(input("Enter amount: "))
    currency = input("Enter currency: ").upper()
    getCurrency(amount, currency)

def getCurrency(amount, currency):

    if currency == "LD" or currency == "LRD" and amount>5:
        print(f"{amount/150} USD")
    
    elif currency == "USD":
        print(f"{amount*150} LD")
main()