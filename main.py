import re  # Import the regular expression module
import functools  # Import functools module for functional tools


def compare(a, b):
    # Custom comparison function for sorting strings
    # It compares two strings character by character and based on certain conditions
    ita = iter(a)  # Create an iterator for string a
    itb = iter(b)  # Create an iterator for string b
    while True:  # Loop indefinitely
        try:
            char_a = next(ita)  # Get the next character of string a
            char_b = next(itb)  # Get the next character of string b

            # Compare characters lexicographically
            if char_a < char_b:
                return -1
            elif char_a > char_b:
                return 1
        except StopIteration:  # Handle StopIteration exception
            # Return the difference in lengths if one string ends before the other
            return len(a) - len(b)


def split_string(str, range_str):
    # Function to split a string into substrings based on given range

    # Declare a list to store the splitted strings
    substrings = []

    # Find all positive numbers within the range_str and put them in a list
    numbers = re.findall(r'\d+', range_str)
    # Convert the numbers from strings to integers
    numbers = [int(num) for num in numbers]
    pos = 0  # Initialize position variable

    # Check for alphabets and numbers
    corr_str = ""
    for i in str:
        if i.isalnum():
            corr_str+=i
    str = corr_str


    # Loop through the string while there are numbers in the range_str
    while pos < len(str) and numbers:
        # Determine the length of the next substring
        length = numbers.pop(0)  # Get the next length from the array
        len_substr = min(length,
                         len(str) -
                         pos)  # Ensure we don't exceed the string length

        # Extract the substring and add it to the list
        substrings.append(str[pos:pos + len_substr])

        # Move to the next position
        pos += len_substr

        # Rotate the lengths array
        numbers.append(length)

    # Sort the array based on the compare function
    substrings.sort(key=functools.cmp_to_key(compare))

    return substrings  # Return the sorted substrings


# Example usage
split_string("abcdEfghijklmnoPqrsTuvwxyz", "4-6")
