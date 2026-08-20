numbers = list(map(int, input("Enter a list (elements space separated): ").split()))

print(numbers)
print("\nEven no's up to 237")

for num in numbers:
    if num == 237:
        break
    if num % 2 == 0:
        print(num, end=" ")
