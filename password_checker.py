#!/usr/bin/env python3
"""
Password Strength Checker
-------------------------
Analyzes a password and rates its strength based on length,
character variety, and common-password checks.

Usage:
    python password_checker.py
"""

import re
from pathlib import Path


def load_common_passwords():
    """Load the list of commonly used passwords."""
    path = Path(__file__).parent / "common_passwords.txt"
    if path.exists():
        return {line.strip().lower() for line in path.read_text().splitlines() if line.strip()}
    return set()


def check_password(password: str, common: set) -> dict:
    """Score a password and return detailed feedback."""
    feedback = []
    score = 0

    # Length checks
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Use 12+ characters for a stronger password.")
    else:
        feedback.append("Too short! Use at least 8 characters (12+ recommended).")

    # Character variety
    checks = [
        (r"[A-Z]", "uppercase letter (A-Z)"),
        (r"[a-z]", "lowercase letter (a-z)"),
        (r"[0-9]", "digit (0-9)"),
        (r"[^A-Za-z0-9]", "special character (!@#...)"),
    ]
    for pattern, label in checks:
        if re.search(pattern, password):
            score += 1
        else:
            feedback.append(f"Add at least one {label}.")

    # Common password check
    if password.lower() in common:
        score = 0
        feedback.append("This is a commonly used password — pick something unique!")

    # Repeated characters
    if re.search(r"(.)\1{2,}", password):
        score = max(0, score - 1)
        feedback.append("Avoid repeating the same character 3+ times.")

    rating = (
        "Very Strong 💪" if score >= 6 else
        "Strong ✅" if score >= 5 else
        "Moderate ⚠️" if score >= 3 else
        "Weak ❌"
    )
    return {"score": score, "rating": rating, "feedback": feedback}


def main():
    common = load_common_passwords()
    print("🔐 Password Strength Checker (type 'quit' to exit)\n")
    while True:
        password = input("Enter a password: ")
        if password.lower() == "quit":
            break
        if not password:
            continue
        result = check_password(password, common)
        print(f"\nScore: {result['score']}/6 — {result['rating']}")
        for tip in result["feedback"]:
            print(f"  • {tip}")
        print()


if __name__ == "__main__":
    main()
