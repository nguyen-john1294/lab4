def main():
    numbers = []
    count = 0
    sum = 0
    while count < 20:
        num = int(input("Enter a Number:"))
        numbers.append(num)
        count += 1
    for e in numbers:
        sum += numbers[e-1]
    sum /= 20
    print(sum)
    print(min(numbers))
    print(max(numbers))    
main()