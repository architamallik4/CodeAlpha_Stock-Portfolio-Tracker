# Stock Portfolio Tracker

A simple console-based Python program that helps users calculate the total value of their stock investments.
The program allows users to enter stock names and quantities, calculates the investment value for each stock, and displays a portfolio summary.

This project was developed as part of the **CodeAlpha Python Programming Internship**.

---

## Features

* Enter multiple stock investments
* Uses a predefined dictionary of stock prices
* Calculates total investment value
* Displays a clear portfolio summary
* Saves the portfolio report to a text file (`portfolio_summary.txt`)
* Input validation for stock names and quantities

---

## Technologies Used

* Python
* Dictionaries
* Functions
* File Handling
* Basic Input / Output

---

## Available Stocks

| Stock Symbol | Price ($) |
| ------------ | --------- |
| AAPL         | 180       |
| TSLA         | 250       |
| GOOGL        | 140       |
| AMZN         | 130       |
| MSFT         | 320       |

---

## How to Run the Program

1. Clone or download this repository.
2. Navigate to the project folder.
3. Run the program using Python:

```bash
python stock_portfolio_tracker.py
```

---

## Example Usage

```text
Enter stock name (or 'done' to finish): AAPL
Enter quantity: 5

Enter stock name (or 'done' to finish): TSLA
Enter quantity: 3

Enter stock name (or 'done' to finish): done
```

Output:

```text
Portfolio Summary
-----------------
AAPL : 5 shares x $180 = $900
TSLA : 3 shares x $250 = $750

Total Investment Value: $1650
```

---

## Output File

After running the program, a file named:

```text
portfolio_summary.txt
```

will be created containing the portfolio summary.

---

## Author

Developed as part of the **CodeAlpha Python Programming Internship Program**.
