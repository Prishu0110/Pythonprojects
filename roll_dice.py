import random

def roll_dice(num_dice):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

def main():
    print("Dice Rolling Simulator")
    print("----------------------")

    try:
        num_dice = int(input("Enter the number of dice to roll: "))
        if num_dice <= 0:
            raise ValueError("Number of dice must be a positive integer.")
        
        # Roll the dice
        dice_results = roll_dice(num_dice)

        # Display the results
        print(f"\nResults of rolling {num_dice} dice:")
        print(" ".join(map(str, dice_results)))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
