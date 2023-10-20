import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("grades.csv")

df['Дата'] = pd.to_datetime(df['Дата'])

df = df.sort_values(by='Дата')

plt.figure(figsize=(10, 6))
plt.plot(df['Дата'], df['Оцінка'], marker='o', linestyle='-')
plt.title('Динаміка оцінок')
plt.xlabel('Дата')
plt.ylabel('Оцінка')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('grades_graph.png')

plt.show()
