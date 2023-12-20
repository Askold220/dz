import seaborn as sns
import matplotlib.pyplot as plt

# Завдання 1
tips = sns.load_dataset("tips")

sns.histplot(tips["total_bill"], kde=True, color="skyblue")
plt.title("Розподіл вартості рахунків")
plt.xlabel("Вартість рахунку")
plt.ylabel("Кількість споживачів")
plt.show()


sns.scatterplot(x="total_bill", y="tip", data=tips, hue="sex", palette="muted")
plt.title("Залежність між вартістю рахунку та чайовими")
plt.xlabel("Вартість рахунку")
plt.ylabel("Чайові")
plt.legend()
plt.show()

total_bill_stats = tips["total_bill"].describe()
tip_stats = tips["tip"].describe()

print("Статистичні показники для вартості рахунку:\n", total_bill_stats)
print("\nСтатистичні показники для чайових:\n", tip_stats)

sns.boxplot(x="day", y="total_bill", data=tips, palette="Set3")
plt.title("Порівняння вартості рахунків за різні дні тижня")
plt.xlabel("День тижня")
plt.ylabel("Вартість рахунку")
plt.show()
