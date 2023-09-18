import psycopg2
import csv


#establishing the connection
conn = psycopg2.connect(database = 'womfootball', user = 'postgres', password = 'noentry', host='127.0.0.1', port= '5432'
)

# CREATING  AN OBJECT CURSOR
cursor = conn.cursor()


# CREATE TABLE
sql_table  = '''
DROP TABLE IF EXISTS goalscores;

CREATE TABLE IF NOT EXISTS goalscores(
gl_id SERIAL PRIMARY KEY, 
date DATE, 
home_team VARCHAR (250), 
away_team VARCHAR (250), 
team VARCHAR (250), 
scorer VARCHAR (250), 
minute INT, 
own_goal BOOLEAN, 
penalty BOOLEAN
)'''


cursor.execute(sql_table)
sql2 = '''COPY goalscores(gl_id, date, home_team, away_team, team, scorer, minute, own_goal, penalty)
FROM 'C:\\Users\\Public\\goalscorers_new.csv'
DELIMITER ','
CSV HEADER;'''
  
cursor.execute(sql2)
  
sql3 = '''select * from goalscores where gl_id < 100;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)
  

conn.commit()
cursor.close()
conn.close()

