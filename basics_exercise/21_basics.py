def check_character_type(char):
    if char.isalpha():
        return f"{char} is an alphabet"
    elif char.isdigit():
        return f"{char} is a digit"
    else:
        return f"{char} is a special character"

# Example usage
char = input("Enter a character: ")
print(check_character_type(char))