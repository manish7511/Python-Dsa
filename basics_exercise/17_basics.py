def check_vowel_consonant(char):
    vowels = 'aeiouAEIOU'
    if char in vowels:
        print(char)
        return f"{char} is a vowel"
    else:
        return f"{char} is a consonant"

char = input("Enter a character: ")
print(check_vowel_consonant(char))