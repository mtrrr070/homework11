from student import (
    students, 
    find_student_by_name, 
    show_all_students, 
    add_student, 
    remove_student, 
    show_students_by_group
)
from utils import input_number, print_line

def show_menu():
    print("===== ЖУРНАЛ СТУДЕНТОВ =====")
    print("1. Показать всех студентов")
    print("2. Найти студента")
    print("3. Добавить оценку")
    print("4. Показать оценки")
    print("5. Показать средний балл")
    print("6. Добавить студента")
    print("7. Удалить студента")
    print("8. Показать студентов по группе")
    print("9. Показать статус студента")
    print("0. Выйти")

def main():
    while True:
        show_menu()
        choice = input("Выберите действие: ")
        
        if choice == "1":
            show_all_students()
        
        elif choice == "2":
            name = input("Введите имя студента: ")
            student = find_student_by_name(name)
            if student is None:
                print("Студент не найден")
            else:
                student.show_info()
        
        elif choice == "3":
            name = input("Введите имя студента: ")
            student = find_student_by_name(name)
            if student is None:
                print("Студент не найден")
            else:
                grade = input_number("Введите оценку от 0 до 100: ", 0, 100)
                student.add_grade(grade)
        
        elif choice == "4":
            name = input("Введите имя студента: ")
            student = find_student_by_name(name)
            if student is None:
                print("Студент не найден")
            else:
                student.show_grades()
        
        elif choice == "5":
            name = input("Введите имя студента: ")
            student = find_student_by_name(name)
            if student is None:
                print("Студент не найден")
            else:
                average = student.get_average_grade()
                print(f"Средний балл: {average:.2f}")
        
        elif choice == "6":
            add_student()
        
        elif choice == "7":
            remove_student()
        
        elif choice == "8":
            show_students_by_group()
        
        elif choice == "9":
            name = input("Введите имя студента: ")
            student = find_student_by_name(name)
            if student is None:
                print("Студент не найден")
            else:
                print(f"Статус: {student.get_status()}")
                print(f"Прошел курс: {student.is_passed()}")
        
        elif choice == "0":
            print("Программа завершена")
            break
        
        else:
            print("Ошибка: такого пункта нет")
        
        print_line()

if __name__ == "__main__":
    main()
