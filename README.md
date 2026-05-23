# ALU Financial Transaction Log - Regex Data Extraction

## How to run it

Make sure you are in the project folder, then run:

```bash
cd src
python main.py
```

Results will be printed in the terminal and also saved to `output/sample-output.json`.

## What does the program extract?

### 1. Email addresses
Only accepts ALU official emails ending with:
- @alueducation.com
- @alumni.alueducation.com
- @si.alueducation.com

Everything else like gmail.com or yahoo.com is ignored.

### 2. Phone numbers
Accepts international phone numbers starting with + or 0.
Rejects fake numbers made of all zeros.

### 3. Credit card numbers
Accepts cards in format: XXXX XXXX XXXX XXXX or XXXX-XXXX-XXXX-XXXX
Only accepts major card types (Visa and Mastercard)
Rejects cards with all repeated digits like 9999-9999-9999-9999.

### 4. Currency amounts
Accepts amounts in $, €, and £.
Rejects zero and negative amounts.
Rejects suspiciously large amounts from hostile records.

## Security awareness

Not all input can be trusted. Our raw text contains:
- SQL injection attempts like `'; DROP TABLE users;--`
- Script injection like `<script>alert('hack')</script>`
- Fake card numbers and zero amounts

The program is designed to ignore all of these and only extract
data that passes our validation rules.

## Project structure
alu-regex-data-extraction/
├── input/
│   └── raw-text.txt      # Raw messy transaction data
├── src/
│   └── main.py           # Main extraction program
├── output/
│   └── sample-output.json # Clean extracted results
└── README.md              
