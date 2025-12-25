if __name__ == "__main__":
    price = float(input("Введите цену: "))
    discount = float(input("Введите скидку: "))
    final_price = price * (1 - discount / 100)

    print("Итоговая цена: ", final_price)
