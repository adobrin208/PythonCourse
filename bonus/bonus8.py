date = input("Enter today is date: ")
mood = input("How do you rate your mood today from 1 to ta? ")
thoughts = input("Let your thoughts flow:\n")

with open(f"../journal/{date}.txt", "w") as file:
    file.write(mood + 2 *"\n")
    file.write(thoughts)