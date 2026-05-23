#!/usr/bin/python3
import re
import json

file = open("../input/raw-text.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()


email_pattern    = r"[a-zA-Z0-9][a-zA-Z0-9._-]*@(alueducation|alumni\.alueducation|si\.alueducation)\.com"
phone_pattern    = r"(\+|0)[0-9-]{9,15}[0-9]"
card_pattern     = r"[0-9]{4}[ -][0-9]{4}[ -][0-9]{4}[ -][0-9]{4}"
currency_pattern = r"[$€£]\d+(,\d+)?(\.\d{2})?"

emails     = []
phones     = []
cards      = []
currencies = []

for line in lines:

    if "Email:" in line:
        email_match = re.search(email_pattern, line)
        if email_match:
            emails.append(email_match.group())

    if "Phone:" in line:
        phone_match = re.search(phone_pattern, line)
        if phone_match:
            number = phone_match.group()
        
            if not all(c in '0-' for c in number):
                phones.append(number)

    if "Card:" in line:
        card_match = re.search(card_pattern, line)
        if card_match:
            card = card_match.group()
            digits_only = card.replace(" ", "").replace("-", "")
            if len(set(digits_only)) > 1 and(digits_only[0] == '4' or digits_only[0] == '5'):
                cards.append(card)

    if "Amount:" in line:
        currency_match = re.search(currency_pattern, line)
        if currency_match:
            amount = currency_match.group()
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
