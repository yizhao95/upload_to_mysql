#!/usr/bin/env python
# coding: utf-8

# In[17]:


from mysql.connector import MySQLConnection, Error
import mysql.connector
from datetime import datetime

def upload(data,column_names = None, tablename = 'table',host='localhost',database='database',user = 'root',password = '123'):
    
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password)
        if connection.is_connected():
            valuelen = (('%s')*len(data))[:-1]
            if column_names != None:
                query ="INSERT INTO " + str(tablename)+' ('+str(column_names)+') ' +"VALUES "+(valuelen)
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute(query, data)
                connection.commit()
                print("Prediction result uploaded")
                
            else:
                query = "INSERT INTO " + str(tablename) +"VALUES "+(valuelen)
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute(query, data)
                connection.commit()
                print("Prediction result uploaded")

    except Error as e:
        print("Error while connecting to MySQL", e)
    
    return


# In[ ]:





# In[ ]:




