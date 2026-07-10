def is_palindrome(num):
    return str(num) == str(num)[::-1]

def print_palindromes(start, end):
    for num in range(start, end + 1):
        if is_palindrome(num):
            print(num)

# Example usage
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print_palindromes(start, end)
