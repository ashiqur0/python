#### Python Match ####

# Python match Statement
day = 4
match day:
    case 1: print("Sunday")
    case 2: print("Monday")
    case 3: print("Tuesday")
    case 4: print("Wednesday")
    case 5: print("Thursday")
    case 6: print("Friday")
    case 7: print("Saturday")

# Default Value : '_' The underscore sign is used as default
match day:
    case 5: print('Thurstday')
    case 6: print('Friday')
    case 7: print('Saturday')
    case _: print('Default value printed')

# Combine Values
match day:
    case 1 | 2 | 3 | 4: print('Today is saturday')
    case 5: print('Today is sunday')
    case _: print('Looking for weekend')
    
# If Statements as Guards
match day:
    case 1 | 2 | 3 | 4 if day > 2: print('A weekday in April')
    case 5: print('A weekday May')
    case _: print('No matcht')