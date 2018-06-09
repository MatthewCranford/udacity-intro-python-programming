# names = input('Enter names seperated by commas: ').split(
#     ',')  # get and process input for a list of names
# # get and process input for a list of the number of assignments
# assignments = input('Enter assignments seperated by commas: ').split(',')
# # get and process input for a list of grades
# grades = input('Enter grades seperated by commas: ').split(',')

names = ['jon', 'rob', 'bran']
assignments = [5, 1, 34]
grades = [75, 90, 32]


# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"


# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)))
