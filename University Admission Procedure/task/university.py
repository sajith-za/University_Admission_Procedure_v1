# write your code here
def initial_code():
    mark = [int(input()) for _ in range(3)]
    mean_score = sum(mark) / len(mark)
    print(mean_score)

    if mean_score >= 60:
        print("Congratulations, you are accepted!")
    else:
        print("We regret to inform you that we will not be able to offer you admission.")


def second_code():
    N = int(input())
    M = int(input())

    student_list = []

    for x in range(N):
        student_list.append(input().split())
        student_list[x][2] = float(student_list[x][2])

    student_list.sort(key=lambda y: (-y[2], y[0], y[1]))

    success_applicant = [student_list[x] for x in range(M)]

    print('Successful applicants:')
    for student in success_applicant:
        print(student[0], student[1])


# Stage 4/7 code tested out ##################################
def read_applicants():
    with open("applicants.txt", "r") as file:
        list_A = file.readlines()

    applicant_list = []

    # Making Test Marks as floats
    for element in list_A:
        list_split = element.split()
        for x in range(2, 7):
            list_split[x] = float(list_split[x])

        # Adding column in order to calculate the mean
        list_split.append(0.00)
        applicant_list.append(list_split)

    return applicant_list


# Sorting the list of applicants according to their relevant departments
def sorting_applicants(N, student_list):
    department_keys = [['Biotech', 2, 3], ['Chemistry', 3, 99], ['Engineering', 5, 4],
                       ['Mathematics', 4, 99], ['Physics', 2, 4]]
    department = {key[0]: [] for key in department_keys}

    # Sorting details
    for x in range(7, 10):
        for dept in department_keys:
            a_list = []
            mod_calculate_mean(student_list, dept[1], dept[2])

            student_list.sort(key=lambda y: (-y[10], y[0], y[1]))

            for i in range(len(student_list)):
                if student_list[i][x] == dept[0] and len(department[dept[0]]) != N:
                    a_list.append(student_list[i])
                    department[dept[0]].append([student_list[i][0], student_list[i][1], student_list[i][10]])

            student_list = [i for i in student_list if i not in a_list]

            if len(student_list) == 0:
                break
    return department


def mod_calculate_mean(students_set, score_1, score_2):
    for i in range(len(students_set)):
        students_set[i][10] = (students_set[i][score_1] + students_set[i][score_2]) / 2 if score_2 != 99 \
            else students_set[i][score_1]

        # Getting the higher score value between mean and special exam
        students_set[i][10] = max(students_set[i][10], students_set[i][6])

    return students_set


# Printing the information
def print_list(output):
    for key, value in output.items():
        print(key)
        value.sort(key=lambda x: (-x[2], x[0], x[1]))

        for element in value:
            print(element[0], element[1], element[2])
        print()


# Writing the information to file
def write_list(output):
    for key, value in output.items():
        print(key)
        value.sort(key=lambda x: (-x[2], x[0], x[1]))

        filename = key + ".txt"
        with open(filename, "w") as file:
            for element in value:
                file.write(str(element[0]) + " " + str(element[1]) + " " + str(element[2]))
                file.write('\n')


# Main code to run program
final_students = sorting_applicants(int(input()), read_applicants())
print_list(final_students)
write_list(final_students)
