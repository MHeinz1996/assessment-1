def optimal_change(item_cost, ammount_paid):
    change = {}
   
    # Calls validity function to test args
    valid = validity(item_cost, ammount_paid)

    if(valid != True):
        return valid

    # Use round() function and multiply by 100 to mitigate floating point arithmetic errors
    leftover = int(round(ammount_paid, 2)*100) - int(round(item_cost, 2)*100)
    
    if(leftover < 0):
        return f"Insufficient funds. The item costs ${item_cost} and you only paid ${ammount_paid}."
    
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

    # Output formatter. Counter variable is used to track where punctuations go.
    counter = 0
    for item in change:
        counter += 1
        
        if(len(change) == 1):
            pass
        elif(counter == len(change)):
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

# Function to test validity of args
def validity(item_cost, ammount_paid):
    
    # Tests to make sure that if arg has decimals, it only goes out to two places
    if '.' in str(item_cost):
            decimal_places_cost = str(item_cost).split('.')
            if (len(decimal_places_cost[1]) > 2):
                return f"Invalid parameter. Parameters must be either an integer or a floating point number (to two decimal places)."

    if '.' in str(ammount_paid):
        decimal_places_paid = str(ammount_paid).split('.')
        if (len(decimal_places_paid[1]) > 2):
            return f"Invalid parameter. Parameters must be either an integer or a floating point number (to two decimal places)."

    # Makes sure that args passed are positive integers or floats
    if((isinstance(item_cost, int) == True or isinstance(item_cost, float) == True) and (isinstance(ammount_paid, int) == True or isinstance(ammount_paid, float))):
        pass
    else:
        return f"Invalid parameter. Parameters must be either an integer or a floating point number (to two decimal places)."

    if(item_cost < 0 or ammount_paid < 0):
        return f"Invalid parameter. Parameters must be positive numbers."

    # If all tests pass, args are valid
    return True