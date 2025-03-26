###############################################
# CSE 231
# Project 2
#
# Algorithm
#   assume stock of 10 of ea kind at start
#   repeatedly prompt user for price in dollars
#   Price entered neg - error message, prompt again
#   prompt for payment amt (dollars)
#   payment insufficient, print error message, prompt again
#   Determine change. Use least number of coins needed to make change based on whats avail
#     print no. of coins dispensed as change and their type
#     if exact payment, print message for "no change"
#     If stock < payment, print error message, stop program
#     just before quitting, print total
###############################################

# purchase price and payment will be kept in cents


quarters = 10
dimes = 10
nickels = 10
pennies = 10
stock = quarters*25 + dimes*10 + nickels*5 + pennies*1

print("Welcome to the change-making program.")
print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))

price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

while price != 'q':
    if float(price) < 0:
        print('Error: purchase price must be non-negative.')
        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))  
        price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")    
    if float(price) > 0:
        price_flt = float(price) 
        price_cents = int(round(price_flt*100)) # convert to cents
        payment_cents = float(input('Input dollars paid (xx.xx): '))*100 # converted to cents
        if payment_cents < price_cents:
            print("Error: insufficient payment.")
            payment_cents = (float(input('Input dollars paid (xx.xx): ')))*100
        if payment_cents == price_cents: 
            print('No change.')
        if payment_cents > price_cents:
            change_cents = payment_cents - price_cents
            if change_cents > 0 and (stock - change_cents > 0):
                # initialize change denominations
                q_chg = 0 # change in quarters
                d_chg = 0 # change in dimes
                n_chg = 0 # change in nickels
                p_chg = 0 # change in pennies
                while quarters > 0 and (change_cents >= 25) and q_chg <= 10:
                    change_cents = change_cents - 25 
                    quarters = quarters - 1
                    q_chg +=1
                    #if q_chg == 10:
                while dimes > 0 and (10 <= change_cents) and d_chg <= 10:
                    change_cents = change_cents - 10
                    dimes = dimes - 1
                    d_chg += 1
                        #if d_chg == 10:
                while nickels > 0 and (change_cents >= 5) and n_chg <= 10:
                    change_cents = change_cents - 5
                    nickels = nickels -1
                    n_chg += 1
                        #if n_chg == 10:
                while pennies > 0 and (change_cents >= 1) and p_chg <= 10:
                    change_cents = change_cents - 1
                    pennies = pennies - 1
                    p_chg += 1
                print('\nCollect change below: ')
                if q_chg > 0:
                    print('Quarters:', q_chg)
                if d_chg > 0:
                    print("Dimes:", d_chg)
                if n_chg > 0:
                    print("Nickels:", n_chg)
                if p_chg > 0:
                    print("Pennies:", p_chg)
                stock = quarters*25 + dimes*10 + nickels*5 + pennies*1
            if change_cents > 0 and (stock - change_cents <= 0):
                print('Error: ran out of coins.')
                break
        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
                quarters, dimes, nickels, pennies))    
        price = input("Enter the purchase price (xx.xx) or 'q' to quit: ") # prompt user again


        