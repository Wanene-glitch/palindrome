def is_palindrome(s):
    s=str(s).lower()
    s=s.replace(" ","")
    return s==s[::-1]
user_input =input("Enter word or number: ")
if is_palindrome(user_input):
    print(f"'{user_input}'is a palindrome.")
else:
    print(f"'{user_input}'is not a palindrome.") 
