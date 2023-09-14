import time
import random

# Text-based dice faces for numbers 1 to 6
dice_faces = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘\n",
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘\n",
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘\n",
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘\n",
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘\n",
    ),
    6: (
        "┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘\n",
    ),
}


def roll_dice_animation(num_faces):
    for _ in range(3):
        result = random.randint(1, num_faces)
        dice_face = dice_faces[result]  # Access the correct face using the result
        print(f"\rRolling...\n{dice_face[0]}\n{dice_face[1]}\n{dice_face[2]}\n{dice_face[3]}\n{dice_face[4]}", end="",
              flush=True)
        time.sleep(0.3)
    return result


def get_valid_input():
    while True:
        try:
            faces = int(input("How many faces would you like on the dice? (Maximum is 6): "))
            if 1 <= faces <= 6:
                return faces
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


while True:
    faces = get_valid_input()

    result = roll_dice_animation(faces)

    print(f"\nThe computer generated the value {result} on a dice with {faces} faces.")

    play_again = input("Roll again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
