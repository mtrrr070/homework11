def input_number(message, min_val=None, max_val=None):
    """
    Функция для безопасного ввода числа.
    Args:
        message: Сообщение пользователю
        min_val: Минимальное значение (опционально)
        max_val: Максимальное значение (опционально)
    Returns:
        int: Введенное число
    """
    while True:
        try:
            value = int(input(message))
            
            if min_val is not None and value < min_val:
                print(f"Ошибка: число должно быть не менее {min_val}")
                continue
            
            if max_val is not None and value > max_val:
                print(f"Ошибка: число должно быть не более {max_val}")
                continue
            
            return value
        except ValueError:
            print("Ошибка: введите число")

def print_line():
    print("-" * 40)
