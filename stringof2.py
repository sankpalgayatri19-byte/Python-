# Get a string from the user
string = input("Enter a string: ")

# Check the length
if len(string) < 2:
    result = ""
else:
    result = string[:2] + string[-2:]

print("Result:", result)
