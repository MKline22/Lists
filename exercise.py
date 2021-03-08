print("Please choose one of the following exercises:\n ")
print("1) Bench press\n 2) Push ups\n 3) Dead lists\n 4) Jumping jax\n 5) Squats")
usrinput = input("Enter choice: ")
workouts = open("workouts.tsv")

workout_lists = []
for line in workouts:
    stripped_list = line.strip()
    full_list = stripped_list.split()
    workout_lists.append(full_list)

workouts.close()

