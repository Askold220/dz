user_info = {}

def registration():
    name = input("Введіть ім'я користувача: ")
    email = input("Введіть електронну пошту: ")
    age = input("Введіть вік користувача: ")

    user_info['name'] = name
    user_info['email'] = email
    user_info['age'] = age

    print("Реєстрація завершена!")

def change_info():
    if 'name' in user_info:
        print("Поточні дані користувача:")
        print(f"Ім'я: {user_info['name']}")
        print(f"Електронна пошта: {user_info['email']}")
        print(f"Вік: {user_info['age']}")
        print("Введіть нові дані:")
        name = input("Нове ім'я користувача (або натисніть Enter, щоб залишити без змін): ")
        email = input("Нова електронна пошта (або натисніть Enter, щоб залишити без змін): ")
        age = input("Новий вік користувача (або натисніть Enter, щоб залишити без змін): ")

        if name:
            user_info['name'] = name
        if email:
            user_info['email'] = email
        if age:
            user_info['age'] = age

        print("Дані користувача оновлені!")

    else:
        print("Користувач не був зареєстрований. Будь ласка, спершу зареєструйтесь.")

while True:
    print("\nМеню:")
    print("1. Реєстрація користувача")
    print("2. Зміна даних користувача")
    print("3. Вихід")
    choice = input("Виберіть опцію: ")

    if choice == '1':
        registration()
    elif choice == '2':
        change_info()
    elif choice == '3':
        break
    else:
        print("Невірний вибір опції. Будь ласка, спробуйте знову.")
