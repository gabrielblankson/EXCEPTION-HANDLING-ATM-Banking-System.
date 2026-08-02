# EXCEPTION-HANDLING-ATM-Banking-System

A simple ATM banking system built with Python's `BankAccount` class, demonstrating exception handling with `try`, `except`, and `finally`.

## Overview

This project simulates basic ATM operations — depositing, withdrawing, and checking balance — while gracefully handling invalid input instead of crashing.

## Features

- `deposit(amount)` — rejects negative deposits (`ValueError`)
- `withdraw(amount)` — rejects invalid amounts (`ValueError`) and withdrawals exceeding the balance (`InsufficientFundsError`)
- `check_balance()` — displays the current balance
- Custom exception `InsufficientFundsError` for failed withdrawals

## Usage

```bash
python bank_account.py
```

## Author

Blankson Kwabena-EL162/234 Object Oriented Programming, Umat
