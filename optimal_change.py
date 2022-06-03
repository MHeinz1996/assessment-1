def optimal_change(item_cost, ammount_paid):
    change = {}
   
    # Use round() function and multiply by 100 to mitigate floating point arithmetic errors
    leftover = int(round(ammount_paid, 2)*100) - int(round(item_cost, 2)*100)

    # Handle invalid inputs
    if(item_cost < 0 or ammount_paid < 0):
        return f"Invalid parameter. Parameters must be positive numbers"
    if(leftover < 0):
        return f"Insufficient funds. The item costs ${item_cost} and you only paid ${ammount_paid}"
    
    # Dict to define monetary denominations with a value
    money = {
        '$100 bill': 10000,
        '$50 bill': 5000,
        '$20 bill': 2000,
        '$10 bill': 1000,
        '$5 bill': 500,
        '$1 bill': 100,
        'quarter': 25,
        'dime': 10,
        'nickel': 5,
        'penny': 1,
    }

    # Fill change dict with optimal change
    while leftover != 0:
        for key in money:
            if (leftover/money[key]) >= 1:
                if key in change:
                    change[key]+=1
                else:
                    change[key] = 1
                leftover -= money[key]
                break

    
    # Initialize an output to be appended to with output formatter
    output = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${ammount_paid} is "

    # Output formatter
    counter = 0
    for item in change:
        counter += 1
        if(counter == len(change)):
            output+= "and "
        if(item != 'penny'):
            if change[item] > 1:
                output += f"{change[item]} {item}s"
            else:
                output += f"{change[item]} {item}"
           
            if counter < len(change):
                output += ", "
            elif counter == len(change):
                output += "."
        else:
            if change[item] > 1:
                output += f"{change[item]} pennies."
            else:
                output += f"{change[item]} penny."
        



    
    return output

# Example of output formatting:
# "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."