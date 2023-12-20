while True:
    try:
        user_input = int(input("Введіть ціле число: "))
        print("Ваше введене ціле число:", user_input)
        break
    except ValueError:
        print("Помилка! Будь ласка, введіть коректне ціле число.")

print("Дякуємо за співпрацю!")
