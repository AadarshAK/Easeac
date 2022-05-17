import pandas as pd
import csv
from datetime import date

today = date.today()
d = today.strftime("%d/%m/%Y")
particulars = int(input('Particulars : '))
mode_of_payment = input('Mode of Payment : ')
amount = int(input('Amount : '))

transaction_code = ['Espana Maintenance',
                    'Wet waste disposal charges',
                    'Electricity Bill',
                    'Car Wash Charges',
                    'Cable (Wizard)',
                    'Cable (Tata Sky)',
                    'Paper Bill',
                    'Telephone Bill (KKV)',
                    'Telephone Bill (AV)',
                    'Telephone Bill (VV)',
                    'Telephone Bill (Landline)',
                    'Internet',
                    'Pharmacy',
                    'Gas',
                    'Groceries',
                    'Milk',
                    'Vegetables',
                    'Fish/Meat']

particulars_str = transaction_code[particulars]

csv_list = {'Date':d, 'Particulars':[particulars_str], 'Mode of Payment':[mode_of_payment], 'Amount':[amount]}
csv_list_df = pd.DataFrame(csv_list, columns=['Date', 'Particulars', 'Mode of Payment', 'Amount'])
print(csv_list_df)

csv_list_df.to_csv(r'MonthlyExpenses.csv', mode='a', header=False, index=False)