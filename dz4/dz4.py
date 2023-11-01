import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import matplotlib.pyplot as plt

credentials_path = 'credentials.json'

spreadsheet_name = 'dz4Python'
worksheet_name = 'dz4Python'

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
gc = gspread.authorize(credentials)

worksheet = gc.open(spreadsheet_name).worksheet(worksheet_name)
data = worksheet.get_all_records()

df = pd.DataFrame(data)

print(df)

plt.figure(figsize=(10, 6))
plt.bar(df['Місяці'], df['Години навчання'], label='Години навчання', color='b', width=0.4)
plt.bar(df['Місяці'], df['Години хобі'], label='Години хобі', color='g', width=0.4, bottom=df['Години навчання'])
plt.xlabel('Місяці')
plt.ylabel('Години')
plt.title('Витрачені години на навчання та хобі за місяць')
plt.legend()
plt.show()
