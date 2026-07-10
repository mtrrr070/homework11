from menu import find_dish_by_id

order = {}
completed_orders = []

MAX_QUANTITY_PER_DISH = 10


def add_to_order(dish_id, quantity):
    dish = find_dish_by_id(dish_id)

    if dish is None:
        print("Блюдо не найдено")
        return

    if quantity <= 0:
        print("Количество должно быть больше 0")
        return

    # Проверка максимального количества одинаковых блюд
    if dish_id in order:
        new_quantity = order[dish_id] + quantity
        if new_quantity > MAX_QUANTITY_PER_DISH:
            print(f"Ошибка: нельзя заказать больше {MAX_QUANTITY_PER_DISH} одинаковых блюд")
            return
        order[dish_id] = new_quantity
    else:
        if quantity > MAX_QUANTITY_PER_DISH:
            print(f"Ошибка: нельзя заказать больше {MAX_QUANTITY_PER_DISH} одинаковых блюд")
            return
        order[dish_id] = quantity

    print(f"Блюдо {dish['name']} добавлено в заказ")


def show_order():
    if len(order) == 0:
        print("Заказ пустой")
        return

    print("===== ВАШ ЗАКАЗ =====")
    total = 0

    for dish_id, quantity in order.items():
        dish = find_dish_by_id(dish_id)
        item_total = dish["price"] * quantity
        total += item_total

        print(
            f"{dish['name']} | "
            f"{quantity} шт | "
            f"{item_total} тг"
        )

    print(f"Итого: {total} тг")


def calculate_total():
    total = 0

    for dish_id, quantity in order.items():
        dish = find_dish_by_id(dish_id)
        total += dish["price"] * quantity

    return total


def remove_from_order(dish_id):
    if dish_id not in order:
        print("Такого блюда нет в заказе")
        return

    del order[dish_id]
    print("Блюдо удалено из заказа")


def change_quantity(dish_id, quantity):
    if dish_id not in order:
        print("Такого блюда нет в заказе")
        return

    if quantity <= 0:
        print("Количество должно быть больше 0")
        return

    if quantity > MAX_QUANTITY_PER_DISH:
        print(f"Ошибка: нельзя заказать больше {MAX_QUANTITY_PER_DISH} одинаковых блюд")
        return

    order[dish_id] = quantity
    print("Количество изменено")


def checkout():
    if len(order) == 0:
        print("Нельзя оформить заказ. Заказ пустой")
        return

    total = calculate_total()
    discount = 0
    final_total = total

    # Скидка 10% если заказ >= 10000 тг
    if total >= 10000:
        discount = total * 0.1
        final_total = total - discount

    # Сохранение заказа в историю
    order_summary = {
        "items": order.copy(),
        "total": total,
        "discount": discount,
        "final_total": final_total
    }
    completed_orders.append(order_summary)

    print("===== ОФОРМЛЕНИЕ ЗАКАЗА =====")
    for dish_id, quantity in order.items():
        dish = find_dish_by_id(dish_id)
        item_total = dish["price"] * quantity
        print(f"{dish['name']} - {quantity} шт. - {item_total} тг")

    print(f"Сумма заказа: {total} тг")

    if discount > 0:
        print(f"Скидка 10%: -{discount} тг")
        print(f"К оплате: {final_total} тг")
    else:
        print(f"К оплате: {final_total} тг")

    print("Спасибо за заказ!")
    order.clear()


def show_order_history():
    if len(completed_orders) == 0:
        print("История заказов пустая")
        return

    print("===== ИСТОРИЯ ЗАКАЗОВ =====")

    for index, completed_order in enumerate(completed_orders, start=1):
        print(f"\nЗаказ номер {index}")
        for dish_id, quantity in completed_order['items'].items():
            dish = find_dish_by_id(dish_id)
            item_total = dish["price"] * quantity
            print(f"  {dish['name']} - {quantity} шт. - {item_total} тг")
        
        print(f"Сумма: {completed_order['total']} тг", end="")
        if completed_order['discount'] > 0:
            print(f" (скидка {completed_order['discount']} тг)")
            print(f"К оплате: {completed_order['final_total']} тг")
        else:
            print()
        print("-" * 40)
