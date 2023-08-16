def collatz(number):
        if (number % 2 == 0):
            print(number // 2)
            return number // 2
        elif (number % 2 == 1):
            print(3 * number + 1)
            return 3 * number + 1
try:
    print("Enter number:")
    userInt = int(input())
    while (True):
        userInt = int(collatz(userInt))
        if (userInt == 1):
            break
except ValueError:
    print("Error: Invalid Value. You did not enter an integer.")