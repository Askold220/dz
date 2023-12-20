import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom'],
    'Age': [20, 22, 21, 23, 24],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Score': [75, 90, 82, 78, 88]
}

students = pd.DataFrame(data)

print("Перші 5 рядків з DataFrame 'students':")
print(students.head())

average_age = students['Age'].mean()
print(f"\nСередній вік студентів: {average_age:.2f} років")

high_score_students = students[students['Score'] > 80]
print("\nСтуденти з оцінкою вище 80:")
print(high_score_students)

students.loc[students['Name'] == 'Anna', 'Score'] = 95
print("\nDataFrame після зміни оцінки для Anna:")
print(students)

ages = students['Age']
print("\nSeries 'ages' на основі стовпця 'Age':")
print(ages)

max_age = ages.max()
print(f"\nМаксимальний вік серед студентів: {max_age} років")

students = students[students['Name'] != 'John']
print("\nDataFrame після видалення рядка з іменем 'John':")
print(students)

students.to_csv('students.csv', index=False)
print("\nDataFrame збережено у файл students.csv")
