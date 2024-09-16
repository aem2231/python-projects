import random

def guessingGame():
    num = random.randint(1,100)
    guess = int(input('Enter a guess, 1-100: '))
    while(guess!=num):
        if guess>num:
            guess = int(input('Too high! Try again: '))
        else:
            guess = int(input('Too low! Try again: '))
    print('Correct!')

def perfectSquare():
    num = int(input('Enter a number: '))
    new_num = num/2
    while(new_num>1):
        if(new_num*new_num == num):
            print(f'{num} is a perfect square!')
            break
        new_num = new_num/2
    if new_num<1:
        print(f'{num} is not a perfect square!')

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def multiples():
    total = 0
    for i in range(1,1000):
        if i%3 == 0:
            total+=i
        elif i%5 == 0:
            total +=i

    print(total)

def evenFibbonacci():
    prev_term = 1
    curr_term = 1
    total = 0
    print(prev_term)
    while (curr_term<4000000):
        next_term = prev_term+curr_term
        if curr_term%2 == 0:
            total+=curr_term
        prev_term=curr_term
        curr_term = next_term
    print(total)

def largestPrimeFactor():
    num = 600851475143
    
def main():
    choice = int(input())
    if choice == 1:
        guessingGame()
    elif choice == 2:
        perfectSquare()
    elif choice == 3:
        findSquareRoot()
    elif choice == 4:
        multiples()
    elif choice == 5:
        evenFibbonacci()

main()