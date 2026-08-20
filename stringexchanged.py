string = input("Enter a string: ")

if len(string) <= 1:
    result = string
else:
    result = string[-1] + string[1:-1] + string[0]

print("String after swapping first and last char: -", result)
