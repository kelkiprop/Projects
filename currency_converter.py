currency = float(input("enter amount to exchange:")) # prompts the user to enter input
unit = input("USD or Ksh?: ") # unit variable takes input string of currency whether in usd/ksh

if unit == "USD" or unit == "usd": #takes both uppercase and lowercase
   exchange_rate = 129.55           
   amount_in_ksh = currency * exchange_rate    #converts usd to ksh
   print(f"{currency} USD is equivalent to {amount_in_ksh:.2f} Ksh")
elif unit == "Ksh" or unit == "ksh":
    exchange_rate = 129.55
    amount_in_usd = currency / exchange_rate    #converts ksh to usd
    print(f"{currency} Ksh is equivalent to {amount_in_usd:.2f} USD")
else:
    print("Invalid currency unit")