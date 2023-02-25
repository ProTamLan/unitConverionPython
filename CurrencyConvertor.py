import requests
from_currency = str(input("Enter the currency you want to convert from: ")).upper()
to_currency = x=str(input("Enter the currency you want to convert to: ")).upper()

amount = float(input("Enter the amount you want to convert: "))
response = requests.get(f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}")
#print("Your total in", x, "is: ", response.status_code)

print(f"{amount} {from_currency} is equal to {response.json()['rates'][to_currency]} {to_currency}")




#set-executionpolicy unrestricted -Scope Process
#.\VirtualEnvironment\Scripts\activate
#pip install requests
#python currencyconvertor.py
#https://youtu.be/snPGUT-Fxa4