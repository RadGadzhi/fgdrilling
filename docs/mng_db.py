import sqlite3
import pandas as pd
from sqlalchemy import create_engine


# Создание подключения к БД (БД будет создана если не существует)
connection = sqlite3.connect('instance/priob_721_30407.db')
connection.close()

gti_data = pd.read_csv('instance/Priob_721_30407_11082021_28082021.csv', sep=';', encoding = "UTF-16")

gti_data['Время сбора данных'] = pd.to_datetime(gti_data['Время сбора данных'], dayfirst=True)

def commit_stmt(db, stmt, values=()):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(stmt,values)
    conn.commit()
    conn.close()
    return None

def exec_stmt(db, stmt):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    data = cursor.execute(stmt).fetchall()
    conn.close()
    return data


# for row in gti_data[['Время сбора данных', 'Глубина, м', 'Вес на крюке, т',
#        'Положение крюка (таль-блока), м', 'Нагрузка на долото, т']].iterrows():

#         commit_stmt('instance/priob_721_30407.db',\
#             """
#             INSERT INTO gti_diag (datetime, MD, Weight, High, Force)
#             VALUES (?,?,?,?,?)
#             """, (row[1]['Время сбора данных'], row[1]['Глубина, м'], 
#                   row[1]['Вес на крюке, т'], row[1]['Положение крюка (таль-блока), м'], 
#                   row[1]['Нагрузка на долото, т']))
        # print(row)


print(gti_data.columns)
e = create_engine('sqlite:///instance/priob_721_30407.db')
gti_data.to_sql(name='gti_data', con=e)

