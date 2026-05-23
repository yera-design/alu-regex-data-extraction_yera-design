#!/usr/bin/python3
import re
import json
# I am opening the raw transaction log file that contains all the messy data
file = open("../input/raw-text.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()
#Regex patterns

# This pattern only accepts ALU official emails
# I made sure it starts with a letter or number to block hostile inputs
# It only allows three domains: alueducation.com, alumni.alueducation.com, si.alueducation.com

email_pattern    = r"[a-zA-Z0-9][a-zA-Z0-9._-]*@(alueducation|alumni\.alueducation|si\.alueducation)\.com"

# Phone numbers can start with + 
# I set the length between 9 and 15 to cover different country formats

phone_pattern    = r"\+[0-9-]{9,15}[0-9]"

# Credit cards follow the format XXXX XXXX XXXX XXXX or XXXX-XXXX-XXXX-XXXX
# Both spaces and hyphens are accepted as separators

card_pattern     = r"[0-9]{4}[ -][0-9]{4}[ -][0-9]{4}[ -][0-9]{4}"

# Currency amounts can be in dollars, euros or pounds
# The decimal part like .00 is optional since not all amounts have it
currency_pattern = r"[$€£]\d+(,\d+)?(\.\d{2})?"

emails     = []
phones     = []
cards      = []
currencies = []

for line in lines:
     # I only check lines that start with "Email:" to avoid picking up emails from hostile inputs

    if "Email:" in line:
        email_match = re.search(email_pattern, line)
        if email_match:
            emails.append(email_match.group())
    #I only check lines that start with "Phone:" to avoid matching dates and other numbers

    if "Phone:" in line:
        phone_match = re.search(phone_pattern, line)
        if phone_match:
            number = phone_match.group()
             #I reject numbers made entirely of zeros, those are clearly fake
            if not all(c in '0-' for c in number):
                phones.append(number)
    

    #I only check lines that start with "Card:" to avoid false matches
    if "Card:" in line:
        card_match = re.search(card_pattern, line)
        if card_match:
            card = card_match.group()
            digits_only = card.replace(" ", "").replace("-", "")
            #I reject cards where all digits are the same like 9999-9999-9999-9999
            # I also only accept cards starting with 4 or 5  which are real card types
            if len(set(digits_only)) > 1 and(digits_only[0] == '4' or digits_only[0] == '5'):
                cards.append(card)

    
     # I only check lines that start with "Amount:" to avoid picking up other numbers

    if "Amount:" in line:
        currency_match = re.search(currency_pattern, line)
        if currency_match:
            amount = currency_match.group()
            #I reject zero and negative amounts
            if float(amount[1:].replace(",", "")) > 0:
                currencies.append(amount)

print("RESULTS")

print("EMAILS:", len(emails))
for email in emails:
    print("  -", email)

print("PHONES:", len(phones))
for phone in phones:
    print("  -", phone)

print("CARDS:", len(cards))
for card in cards:
    print("  -", card)

print("CURRENCIES:", len(currencies))
for currency in currencies:
    print("  -", currency)



output = {
    "emails": emails,
    "phones": phones,
    "cards": cards,
    "currencies": currencies
}

output_file = open("../output/sample-output.json", "w", encoding="utf-8")
json.dump(output, output_file, indent=4, ensure_ascii=False)
output_file.close()

print("Results saved")
