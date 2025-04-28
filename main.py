def total_revenue(purchases):
    total_revenue = sum(purchase["quantity"] * purchase["price"] for purchase in purchases)
    return f"Общая выручка:  {total_revenue}"


def items_by_category(purchases):
    result = {}
    for purchase in purchases:
        category = purchase['category']
        if category not in result:
            result[category] = set()
        result[category].add(purchase['item'])
    # Преобразуем множества обратно в списки
    result = {k: list(v) for k, v in result.items()}
    return f"Товары по категориям: {result}"


def expensive_purchases(purchases, min_price):
    expensive_purchases = [purchase for purchase in purchases if purchase['price'] >= min_price]
    return f"Покупки дороже {min_price}: {expensive_purchases}"


def average_price_by_category(purchases):
    result = {}
    for purchase in purchases:
        category = purchase['category']
        if category not in result:
            result[category] = list()
        result[category].append(purchase['price'])

    result = {k: sum(v)/len(v) for k, v in result.items()}
    return f"Средняя цена по категориям: {result}"

def most_frequent_category(purchases):
    result = {}
    for purchase in purchases:
        category = purchase['category']
        if category not in result:
            result[category] = purchase['quantity']
        result[category] += purchase['quantity']

    most_freq_cat = max(result, key=result.get)
    return f"Категория с наибольшим количеством проданных товаров: {most_freq_cat}"


if __name__ == "__main__":
    purchases = [
        {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
        {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
        {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
        {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
    ]
    print(total_revenue(purchases))
    print(items_by_category(purchases))
    print(expensive_purchases(purchases, 1.0))
    print(average_price_by_category(purchases))
    print(most_frequent_category(purchases))