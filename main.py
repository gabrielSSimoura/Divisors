# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
#  (If you don’t know what a divisor is, it is a number that divides evenly into another number.
#  For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


def getDivisors(userNumber):
    divisorsList = range(2, userNumber)

    for item in divisorsList:
        if ((userNumber % item) == 0):
            print(item)


def main():
    userNumber = int(input("Digite um numero: "))

    getDivisors(userNumber)


main()
