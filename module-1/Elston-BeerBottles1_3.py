# Tanner Elston 
# 10/24/25 
# Bottles of Beer on the Wall
# Assignment 1.3

def countdown(bottles):
# While bottles is greater than zero, bottles decrease by one. The decision structure identifies when bottles == 1 is False and applies 's'
    while bottles > 0:
        if bottles > 1:
            print(f'{bottles} bottles of beer on the wall, {bottles} bottles of beer.')
            bottles -= 1
            print(f'Take one down and pass it around, {bottles} bottle{'' if bottles == 1 else 's'} of beer on the wall.\n')

# When bottle == 1, bottles is changed to bottle in the first string. The second string requires no decision for 's'
        else:
            print(f'{bottles} bottle of beer on the wall, {bottles} bottle of beer.')
            bottles -= 1
            print(f'Take one down and pass it around, {bottles} bottles of beer on the wall.\n')

def main():
# Looping input error handling, accepts only natural numbers 1,2,3... etc. Breaks into except ValueError for other characters.
    while True:
        try:
            bottles = int(input("How many bottles of beer are on the wall? "))
            if bottles <= 0:
                print("Please input a natural number.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")


# Executes countdown function and ends with special print statement.
    countdown(bottles)
    print('Time to buy more bottles of beer.')

if __name__ == '__main__':
    main()
