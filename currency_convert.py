def convert(num):
    num_str = str(num)
    result = ""
    count = 0
    index = 0

    while index < len(num_str):
        if count == 1:
            result += ","
            count = 2
        elif count > 1 and count % 2 == 0:
            result += ","

        result += num_str[index]
        count += 1
        index += 1

    return result


number = 504678
indian_currency = convert(number)
print(f'desired_notation --> {indian_currency[:-2]}')



#Explanations
"""
def convert_to_indian_currency(num):
    num_str = str(num)  
    result = ""
    count = 0
    index = len(num_str) - 1 
The function convert_to_indian_currency takes an integer num as input and converts it to Indian currency notation.
num_str = str(num) converts the input number to a string. We no longer reverse the string here, as we'll iterate from the last character.
result, count, and index are initialized to empty string, 0, and len(num_str) - 1 respectively. result will store the final Indian currency notation, count keeps track of the number of digits encountered, and index starts from the last character of the string.

    while index >= 0:
        if count == 1:
            result = "," + result
        elif count > 1 and count % 2 == 0:
            result = "," + result

        result = num_str[index] + result
        count += 1
        index -= 1
The while loop is used to iterate through each character in the num_str string, starting from the last character.
The first if condition if count == 1: checks if the count is equal to 1. If so, it means we have encountered the first digit, and we add a comma (",") to the beginning of the result.
The elif condition elif count > 1 and count % 2 == 0: checks if the count is greater than 1 and divisible by 2. If so, it means we have encountered a digit after the first one, and we add a comma to the beginning of the result.
In both cases, we then concatenate the current character num_str[index] to the beginning of the result.
Finally, we increment the count and decrement the index variables to move towards the first character.

    return result
After the loop, we return the result string, which represents the Indian currency notation.


"""