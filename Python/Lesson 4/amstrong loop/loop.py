start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Armstrong numbers between {start} and {end} are:")

for num in range(start, end + 1):
    digits = str(num)
    num_digits = len(digits)
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    if armstrong_sum == num:
        print(num)
