import sqlite3

conn = sqlite3.connect('metal-archives.db')

conn.execute('''CREATE TABLE band_info
         (
         band_id INTEGER PRIMARY KEY AUTOINCREMENT,
         band_name VARCHAR(100) NOT NULL,
         url VARCHAR(100) NOT NULL,         
         country_of_origin VARCHAR(100), 
         location VARCHAR(100), 
         status VARCHAR(100), 
         formed_in VARCHAR(100), 
         genre VARCHAR(100), 
         lyrical_themes VARCHAR(100), 
         current_label VARCHAR(100), 
         years_active VARCHAR(100),
         data_retrieved DATE
         );''')

conn.close()