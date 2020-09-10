# upload_to_mysql
a quick method used to upload data to mysql

This is used for a quick uploading of data to mysql database.

HOW TO USE:

from upload_to_mysql import upload

upload(data = data,tablename=tablename,column_names = column_names,host='localhost',database='database',user = 'root',password = '123')

##column_names is optional, only use it when uploading data number does not mathc the number of column and you want to specify the which columns you want to add data.
