workouts = open("workouts.tsv")

workout_lists = []
for line in workouts:
    stripped_list = line.strip()
    full_list = stripped_list.split()
    workout_lists.append(full_list)

workouts.close()

