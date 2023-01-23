routine = input("Write the workout routine: ")
print()

routine_name = routine[0:routine.find(":")]
routine_sets = routine[routine.find(":")+1:routine.find("x")]
routine_reps = routine[routine.find("x")+1:routine.find(",")]
routine_rest = routine[routine.find(",")+1:]

print("Perform " + routine_sets + " sets of " + routine_name + " at " + routine_reps + " reps each.")
print("Rest for " + routine_rest + " between each set.")