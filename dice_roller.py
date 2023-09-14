from random import randint

def get_valid_input():
    while True:
        try:
            faces = int(input("How many faces would you like on the dice? (Maximum is 10): "))
            if 1 <= faces <= 10:
                return faces
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def roll_dice(num_faces):
    return randint(1, num_faces)

while True:
    faces = get_valid_input()
    result = roll_dice(faces)
    print(f"The computer generated the value {result} on a dice with {faces} faces.")

    play_again = input("Roll again? (yes/no): ").lower()
    if play_again != 'yes':
        break
