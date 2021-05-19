def card_check(card_num):
    #Implementation of the Luhn algorithm for a credit card
        # From the rightmost digit (excluding the final check digit) and moving left, double the value of every second digit
        # If the result of this doubling operation is greater than 9, then add the digits of the result
        # Take the sum of all the digits (including the check digit).
        # If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn formula; otherwise it is not valid

    if (type(card_num)) != int:
        print("Please enter a valid card number of all digits")
    digits = [int(x) for x in str(card_num)]
    digits_rev = digits[::-1]
    #Include the check digit
    luhn_digits = [digits_rev[0]]
    #For the reversed number begin with the first digit after the check digit, and then every second digit do the doubling operation, summing the resulting digits if 10 or more
    for n in range(1,len(digits_rev)):
        if n%2 == 1:
            doubled = digits_rev[n] * 2
            if doubled >= 10:
                luhn_digits.append(doubled-9)
            else:
                luhn_digits.append(doubled)
        if n%2 == 0:
            luhn_digits.append(digits_rev[n])
    if sum(luhn_digits)%10 == 0:
        print("Valid")
    else:
        print("Invalid")
    
#valid check
card_check(5258901506176905)
#invalid check
card_check(5258910506176905)