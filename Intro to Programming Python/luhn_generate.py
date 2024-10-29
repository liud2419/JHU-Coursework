card_number = input("Please enter an identifier number: ") # prompt for user input

card_number = list(card_number) # turn user input into a list 
inv_card_number = card_number[::-1] # inverse the list

digit_sum = 0 # initialize digit_sum

for i in range(len(inv_card_number)): # for loop where i for the length of the var inv_card_number
        
    digit = int(inv_card_number[i]) 

    if i % 2 == 0: # if the position of i divides 2 with no remainder
        digit *= 2 # multiply the digit by 2 and set it equal to digit
        if digit > 9: # if the digit is bigger than 9 aka 2 digits
            first_digit = digit // 10 # obtain the tenth digit 
            second_digit = digit % 10 # obtain the singles digit
            digit = first_digit + second_digit # sum up the tenth digit and singles digit and set it equal to digit 
    # even positioned numbers get directly added to digit_sum    
    digit_sum += digit # add digit to digit_sum and set equal to digit_sum

check_digit = str((10 - (digit_sum % 10))) # calculate check_digit which is the last digit of a CC number

card_number ="".join(card_number) # turn list back into a string

print("The valid credit card number is: " + card_number + check_digit + " and the newly computed check digit is: " + check_digit) # print statement