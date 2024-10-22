def print_formatted(number):
    # Determine the width of the binary representation of the maximum number
    width = len(bin(number)) - 2  # bin(number) returns a string like '0b101', so remove the '0b'
    
    for i in range(1, number + 1):
        # Print the values in the required formats with proper spacing and alignment
        print(width)

# Example Usage:
n = int(input())
print_formatted(n)

# f"{i:{width}d}": This formats the number i as a decimal, with a width that matches the width of the binary representation of n.
# f"{i:{width}o}": This formats the number i as an octal number.
# f"{i:{width}X}": This formats the number i as a hexadecimal number (capitalized).
# f"{i:{width}b}": This formats the number i as a binary number.