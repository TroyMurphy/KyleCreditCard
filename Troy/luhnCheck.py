def number_check(existingValues, isAlternate=False, sum=0):
    if len(existingValues) == 0:
        valid = sum % 10 == 0
        print("Valid" if valid else "Invalid")
        return valid

    activeDigit = int(existingValues[-1]) * (2 if isAlternate else 1)
    rest = existingValues[:-1]

    return number_check(rest, not(isAlternate), sum + (activeDigit // 10 + activeDigit % 10))
