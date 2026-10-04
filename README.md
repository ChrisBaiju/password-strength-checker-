# 🔐 Password Strength Checker

A simple Python tool that analyzes password strength and gives actionable feedback — great for learning input validation, regex, and security basics.

## Features

- Scores passwords from 0–6 based on length and character variety
- Detects commonly used passwords (checks against a built-in list)
- Flags repeated characters
- Gives specific tips to improve weak passwords

## Usage

```bash
python password_checker.py
```

```
🔐 Password Strength Checker (type 'quit' to exit)

Enter a password: password123

Score: 2/6 — Weak ❌
  • Use 12+ characters for a stronger password.
  • Add at least one uppercase letter (A-Z).
  • Add at least one special character (!@#...).
```

## What I learned

- Regular expressions for pattern matching
- Reading files in Python (`pathlib`)
- Writing clean, testable functions

## Tech

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
