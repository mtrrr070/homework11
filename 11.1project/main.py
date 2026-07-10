from menu import show_menu, search_dish_by_name, filter_dishes_by_category, show_categories
from order import (
    add_to_order,
    show_order,
    checkout,
    remove_from_order,
    change_quantity,
    show_order_history
)
from utils import input_number, print_line


def show_main_menu():
    print("===== КАФЕ =====")
    print("1. Показать меню")
    print("2. Найти блюдо")
    print("3. Добавить блюдо в заказ")
    print("4. Показать заказ")
    print("5. Оформить заказ")
    print("6. Удалить блюдо из заказа")
    print("7. Изменить количество блюда")
    print("8. Фильтр по категории")
    print("9. История заказов")
    print("10. Показать категории")
    print("0. Выйти")


def print_dishes(dishes):
    if len(dishes) == 0:
        print("Ничего не найдено")
        return

    for dish in dishes:
        print(
            f"{dish['id']}. {dish['name']} | "
            f"{dish['price']} тг | "
            f"{dish['category']}"
        )


def main():
    while True:
        show_main_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            show_menu()

        elif choice == "2":
            query = input("Введите название блюда: ")
            results = search_dish_by_name(query)
            print_dishes(results)

        elif choice == "3":
            dish_id = input_number("Введите id блюда: ")
            quantity = input_number("Введите количество: ")
            add_to_order(dish_id, quantity)

        elif choice == "4":
            show_order()

        elif choice == "5":
            checkout()

        elif choice == "6":
            dish_id = input_number("Введите id блюда: ")
            remove_from_order(dish_id)

        elif choice == "7":
            dish_id = input_number("Введите id блюда: ")
            quantity = input_number("Введите новое количество: ")
            change_quantity(dish_id, quantity)

        elif choice == "8":
            category = input("Введите категорию: ")
            results = filter_dishes_by_category(category)
            print_dishes(results)

        elif choice == "9":
            show_order_history()

        elif choice == "10":
            show_categories()

        elif choice == "0":
            print("Программа завершена")
            break

        else:
            print("Ошибка: такого пункта нет")

        print_line()


if __name__ == "__main__":
    main()
