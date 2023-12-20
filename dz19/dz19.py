import matplotlib.pyplot as plt
import numpy as np

# Завдання 1:
months = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень']
sales = [120, 150, 90, 110, 130]

plt.figure(figsize=(8, 6))
plt.plot(months, sales, marker='o', linestyle='-')
plt.title('Кількість продаж за місяць')
plt.xlabel('Місяць')
plt.ylabel('Кількість продаж')
plt.grid(True)
plt.show()

# Завдання 2: 
data1 = np.random.rand(10)
data2 = np.random.rand(10)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.plot(data1, label='Дані 1', marker='o')
ax1.set_title('Підграфіка 1')
ax1.legend()

ax2.plot(data2, label='Дані 2', linestyle='--', marker='x')
ax2.set_title('Підграфіка 2')
ax2.legend()

plt.show()

#завдання 3
data_distribution = np.random.randn(1000)

plt.figure(figsize=(8, 6))
plt.hist(data_distribution, bins=20, color='skyblue', edgecolor='black')
plt.title('Розподіл даних')
plt.xlabel('Значення')
plt.ylabel('Частота')
plt.grid(True)
plt.show()

#завдання 4
variable1 = np.random.rand(50)
variable2 = 2 * variable1 + np.random.randn(50)

plt.figure(figsize=(8, 6))
plt.scatter(variable1, variable2, label='Залежність', color='orange', marker='o')
plt.title('Залежність між двома змінними')
plt.xlabel('Змінна 1')
plt.ylabel('Змінна 2')
plt.legend()
plt.grid(True)
plt.show()

# Додаткове завдання 1: 
categories = ['Категорія A', 'Категорія B', 'Категорія C', 'Категорія D']
counts = [30, 45, 20, 35]

plt.figure(figsize=(8, 6))
plt.bar(categories, counts, color='green', edgecolor='black')
plt.title('Розподіл категоріальних даних')
plt.xlabel('Категорія')
plt.ylabel('Кількість')
plt.grid(axis='y')
plt.show()
