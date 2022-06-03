from optimal_change import optimal_change


print("1:", optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")
print("2:", optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")
print("3:", optimal_change(36.23, 20.67) == "Insufficient funds. The item costs $36.23 and you only paid $20.67.")
print("4:", optimal_change(36.23, -20.67) == "Invalid parameter. Parameters must be positive numbers.")
print("5:", optimal_change(36.23, '50.67') == "Invalid parameter. Parameters must be either an integer or a floating point number (to two decimal places).")
print("6:", optimal_change(93.121234, 123.42353) == "Invalid parameter. Parameters must be either an integer or a floating point number (to two decimal places).")
print("7:", optimal_change(.01, .02) == "The optimal change for an item that costs $0.01 with an amount paid of $0.02 is 1 penny.")
print("This next test might take a little bit longer:")
print("8:", optimal_change(123456789, 987654321) == "The optimal change for an item that costs $123456789 with an amount paid of $987654321 is 8641975 $100 bills, 1 $20 bill, 1 $10 bill, and 2 $1 bills.")