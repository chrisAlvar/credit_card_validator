# Making my variables.
oddDigits = 0
evenDigits = 0
total = 0

# Making input for user to inter a credit card number.
cardNumber = input("Pleas enter a Card number: ")

# Removing any spaces or dash that a user may input within their card number to make it easier to calculate.
cardNumber = cardNumber.replace("-", "")
cardNumber = cardNumber.replace(" ", "")

# Reversing the card number to apply the Luhn's law.
cardNumber = cardNumber[::-1]

# Leaving the odd sets of digits by them self but staring at index 2(the third place) of the numbers based on Luhn's Law.
for x in cardNumber[::2]:
    oddDigits += int(x)

# Doubling the even sets of digits and making an if statement if the doubled number has two digits to add the frist digit by the secound.
for x in cardNumber[1::2]:
    x = int(x) * 2
    if x >= 10:
        evenDigits += (1 + (x % 10))
    else:
        evenDigits += x

# Adding all digits together to get total.
total = oddDigits + evenDigits

# Checking for validation based if the total has no remainder then its valid, if it does have a remainder, its invalid.
if total % 10 == 0:
    print(f"The card number you entered ending in: {cardNumber[3::-1]} \nis VALID.")
else:
    print(f"The card number you entered ending in: {cardNumber[3::-1]} \nis INVALID.")