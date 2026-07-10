dishes = [
    {
        "id": 1,
        "name": "Пицца Маргарита",
        "price": 2500,
        "category": "Пицца"
    },
    {
        "id": 2,
        "name": "Пицца Пепперони",
        "price": 3000,
        "category": "Пицца"
    },
    {
        "id": 3,
        "name": "Пицца Четыре сыра",
        "price": 3200,
        "category": "Пицца"
    },
    {
        "id": 4,
        "name": "Бургер с говядиной",
        "price": 1800,
        "category": "Бургеры"
    },
    {
        "id": 5,
        "name": "Куриный бургер",
        "price": 1500,
        "category": "Бургеры"
    },
    {
        "id": 6,
        "name": "Двойной бургер",
        "price": 2200,
        "category": "Бургеры"
    },
    {
        "id": 7,
        "name": "Цезарь",
        "price": 1600,
        "category": "Салаты"
    },
    {
        "id": 8,
        "name": "Греческий салат",
        "price": 1400,
        "category": "Салаты"
    },
    {
        "id": 9,
        "name": "Салат с курицей",
        "price": 1700,
        "category": "Салаты"
    },
    {
        "id": 10,
        "name": "Латте",
        "price": 900,
        "category": "Напитки"
    },
    {
        "id": 11,
        "name": "Капучино",
        "price": 850,
        "category": "Напитки"
    },
    {
        "id": 12,
        "name": "Чай",
        "price": 600,
        "category": "Напитки"
    },
    {
        "id": 13,
        "name": "Чизкейк",
        "price": 1200,
        "category": "Десерты"
    },
    {
        "id": 14,
        "name": "Тирамису",
        "price": 1300,
        "category": "Десерты"
    },
    {
        "id": 15,
        "name": "Панна-котта",
        "price": 1100,
        "category": "Десерты"
    }
]


def show_menu():
    print("===== МЕНЮ КАФЕ =====")

    for dish in dishes:
        print(
            f"{dish['id']}. {dish['name']} | "
            f"{dish['price']} тг | "
            f"{dish['category']}"
        )


def find_dish_by_id(dish_id):
    for dish in dishes:
        if dish["id"] == dish_id:
            return dish

    return None


def search_dish_by_name(query):
    results = []

    for dish in dishes:
        if query.strip().lower() in dish["name"].lower():
            results.append(dish)

    return results


def filter_dishes_by_category(category):
    results = []

    for dish in dishes:
        if dish["category"].lower() == category.strip().lower():
            results.append(dish)

    return results


def show_categories():
    categories = set()
    for dish in dishes:
        categories.add(dish["category"])
    print("===== КАТЕГОРИИ =====")
    for category in sorted(categories):
        print(f"- {category}")
