if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    # print(student_marks)
    query_name = input()
    average = (sum(student_marks[query_name]))/len(student_marks[query_name])
    print(f'{average:.2f}')

# if __name__ == '__main__':
#     n = int(input('Enter no. of students: '))
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input('Enter students name and marks: ').split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     # print(student_marks)
#     query_name = input('Enter student name whose average marks wants to calculate: ')
#     average = (sum(student_marks[query_name]))/len(student_marks[query_name])
#     print(f'{average:.2f}')
