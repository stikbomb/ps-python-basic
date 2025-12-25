if __name__ == "__main__":
    food_spending = float(input("Введите траты на еду: "))
    transport_spending = float(input("Введите траты на транспорт: "))
    entertainment_spending = float(input("Введите траты на развлечения: "))

    sum_spending = food_spending + transport_spending + entertainment_spending
    average_spending = sum_spending / 3

    print("Общие траты: ", sum_spending)
    print("Средние траты: ", average_spending)
