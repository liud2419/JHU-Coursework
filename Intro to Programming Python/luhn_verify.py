input_count = 0 # initialize inout_count
while input_count < 2: # while loop ends after 2 user inputs
    card_number = input("Please enter a credit card number: ") # prompt for user input

    card_number = str(card_number) # make user input into a string
        
    digit_sum = 0 # initialize digit_sum

    for i in range(len(card_number)): # for loop where i for the length of card_number
        
        digit = int(card_number[i])
        
        if i % 2 == 0: # if the position of i divides 2 with no remainder
            digit *= 2 # multiply the digit by 2 and set it equal to digit
            if digit > 9: # if the digit is bigger than 9 aka 2 digits
                first_digit = digit // 10 # obtain the tenth digit 
                second_digit = digit % 10 # obtain the singles digit
                digit = first_digit + second_digit # sum up the tenth digit and singles digit and set it equal to digit
        # even positioned numbers get directly added to digit_sum 
        digit_sum += digit # add digit to digit_sum and set equal to digit_sum

    if digit_sum % 10 == 0: # if digit_sum can be divided with no remainder 
        validity = "a valid" # set validity to "a valid"
    else: # otherwise
        validity = "an invalid" # set validity to "an invalid"
    
    check_sum = str(digit_sum % 10) # set remainder equal to check_sum

    print("Checksum = " + check_sum) # print statement
    print(card_number + " is " + validity + " CC number.") # print statement
    input_count += 1 # add 1 to input_count after 1 iteration of the entire code