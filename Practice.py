grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Hendrik', 'Aaron'}
# средний балл = последовательная операция над каждым подсписком в списке.
# grades_students - временная переменная в которой хранится подсписок.
# for - повторяет вычисление.
# in - заменяет старое значение на новое в переменной grades.
average_score = [sum(grades_students) / len(grades_students) for grades_students in grades]
# подготовка переменной students = меняем множество на список.
students = list(students)
# сортирует по алфавиту.
students.sort()
# zip - объединяет переменные students и average_score за тем dict преобразует результат в словарь.
Athestational_journal = dict(zip(students, average_score))
# выводит результат на экран.
print('Аттестационный журнал:', Athestational_journal)
number_of_new_students = int(input("Сколько новых учеников вы хотите добавить? "))
# Запускает цикл для повторного запроса ввода новых учеников.
# number_of_new_students указывает количество срабатываний повторного запроса
for _ in range(number_of_new_students):
    # добавляю возможность внести новых или забытых студентов
    new_student = input('введите имя ученика:')
    # добавляю возможность написать его оценки
    # .split разбивает список на отдельные элементы. В данном случае меняет пробелы на запятые
    new_grades = input('введите его оценки через пробел:').split()
    # int преобразует строку в число
    new_grades = [int(grades) for grades in new_grades]
    # добавляет в конец списка нового ученика и его оценки
    students.append(new_student)
    grades.append(new_grades)
# повтаряю операцию по расчету, сортировке, объединению, преобразованию в список и выводу Атестата с правками
average_score = [sum(grades_students) / len(grades_students) for grades_students in grades]
students.sort()
Athestational_journal = dict(zip(students, average_score))
print('Аттестационный журнал:', Athestational_journal)