import psycopg2
###################  TASK 1       ################################
# work=psycopg2.connect('dbname=workshop user=postgres host=localhost port=5432 password=1997')
# jobs=work.cursor()

# def show(cursor):
#     length=20
#     print(*[desc[0].ljust(20) for desc in cursor.description],sep='')
#     print('-'*140)
#     result=jobs.fetchall()
#     for row in result:
#         for col in row:
#             print(str(col).ljust(length)[:17],end='')
#         print()


# number="""
# CREATE TABLE job(
# id SERIAL PRIMARY KEY,
# title TEXT,
# gain INT,
# expiration_date DATE,
# lang BOOLEAN,
# city VARCHAR(20)
# );
# """ 


# number="""
# ALTER TABLE job DROP COLUMN city;
# ALTER TABLE job RENAME gain TO salary;
# ALTER TABLE job ADD company VARCHAR(50);
# """
# jobs.execute(number)


# info_list = [
   
#     ('iOS developer', 3500, '2022-07-18', True, 'A2Z Technologies'),
#     ('Tender üzrə mütəxəssis', 1500, '2022-06-11', False, 'A2Z Technologies'),
#     ('Məlumat bazası üzrə inzibatçı', 1500, '2022-07-12', True, 'ABB ASC'),
#     ('Database Administrator', 2500, '2022-07-14', True, 'A2Z Technologies'),
#     ('Front-End Developer', 1500, '2022-07-23', False, 'AzəriMed QSC'),
#     ('Proqram təminatının testləşdirilməsi üzrə mühəndis', 1500, '2022-08-10', False,'ABB ASC'),
#     ('Back-end üzrə proqramçı', 4100, '2022-07-11', True, 'ABB ASC'),
#     ('Biznes analitika üzrə Baş mütəxəssis ', 2200, '2022-07-03', True, 'ABB ASC'),
#     ('Android proqramçı', 1300, '2022-07-22', True, 'ABB ASC'),
#     ('Front-end üzrə proqramçı', 3200, '2022-07-06', True, 'ABB ASC'),
#     ('Full stack PHP proqramçı', 2400, '2022-07-17', False, 'AzəriMed QSC'),
#     ('Avtomatlaşdırılmış əməliyyat sistemi üzrə proqramçı', 2700, '2022-07-15', True,'ABB ASC'),
#     ('Proqram təminatı üzrə mühəndis', 2700, '2022-07-13', False, 'Kontakt Home'),
#     ('Hüquqşünas', 1500, '2022-07-03', False, 'Kontakt Home'),
#     ('Çatdırılma xidmətləri üzrə fəhlə', 500, '2022-07-15', True, 'Kontakt Home'),
#     ('PHP developer', 1500, '2022-07-11', True, 'ARIS'),
#     ('Məhsul üzrə menecer', 2800, '2022-07-05', True, 'Kontakt Home'),
#     ('Proqram təminatı üzrə aparıcı mühəndis', 2500, '2022-07-02', False,'Kontakt Home'),
#     ('İT sənədləşməsi üzrə mütəxəssis', 1500, '2022-07-25', True, 'Azericard'),
#     ('Information Security Specialist', 2500, '2022-07-03', False, 'DEFSCOPE LLC'),
#     ('IT Helpdesk', 1500, '2022-07-30', True, 'Azericard'),
#     ('Cybersecurity Business Development Internship', 2900, '2022-07-19', False,'DEFSCOPE LLC'),
#     ('Vue.js developer', 1500, '2022-07-29', True, 'ARIS')
# ]
# number="""
# INSERT INTO job(title,salary,expiration_date,lang,company)
# VALUES (%s,%s,%s,%s,%s)
# """
# for info in info_list:
#     jobs.execute(number,info)


# 1
# number="SELECT * FROM job WHERE company='ABB ASC'"
# 2
# number="SELECT * FROM job WHERE company='ABB ASC' AND salary<2000"
# 3
# number="SELECT * FROM job WHERE company='Kontakt Home' AND expiration_date < '2022-07-10'"
# 4
# number="SELECT * FROM job WHERE lang=False AND salary>2500" 
# 5
# number="SELECT * FROM job WHERE title LIKE '%proqramçı' "
# 6
# number="SELECT * FROM job WHERE title NOT LIKE '%end'"
# 7
# number="SELECT * FROM job WHERE title LIKE 'İT%' OR title LIKE 'IT%' "
# 8
# number="SELECT * FROM job WHERE lang=TRUE ORDER BY salary ASC"
# 9
# number="SELECT * FROM job WHERE salary=(SELECT Max(salary) FROM job)"
# 10
# number="SELECT * FROM job WHERE id BETWEEN 2 AND 5 ORDER BY expiration_date>='2022-07-10' ASC "
# 11
# number="SELECT * FROM job WHERE lang=FALSE AND title LIKE '%developer%' OR title LIKE '%proqramçı%'"
# 12
# number = "SELECT * FROM job WHERE company IN ('Kontakt Home', 'AzəriMed QSC', 'A2Z Technologies') AND salary BETWEEN 2500 AND 3000"
# 13
# number="SELECT * FROM job WHERE company='ABB ASC' AND expiration_date<'2022-07-10'"
# 14
# number="SELECT * FROM job WHERE salary=(SELECT Min(salary) FROM job WHERE lang=TRUE)"
# 15
# number="SELECT * FROM job WHERE salary=(SELECT Max(salary) FROM job WHERE lang=FALSE)"
# 16
# number="SELECT Avg(salary) FROM job WHERE title LIKE '%developer%' OR title LIKE '%proqramçı%'"
# 17
# number="SELECT Sum(salary) FROM job WHERE company IN ('Kontakt Home', 'AzəriMed QSC', 'A2Z Technologies')"

# jobs.execute(number)
# result=jobs.fetchall()
# print(result)
# work.commit()
###################################################################



#############  TASK 2    ########################################

# conn=psycopg2.connect('dbname=movie_db user=postgres host=localhost port=5432 password=1997')
# cur=conn.cursor()
# query="""
# CREATE TABLE movie(
# id SERIAL PRIMARY KEY,
# title VARCHAR(50),
# description TEXT,
# follow INT DEFAULT 0,
# gener_id INT,
# release DATE,
# has_fragman BOOLEAN

# );

# """
# data=[
#   {
#     "id": 1,
#     "title": "The Avengers",
#     "description": "Earth's mightiest heroes must come together to save the world from a powerful threat.",
#     "follow": 1000,
#     "gener_id": 1,
#     "release": "2012-05-04",
#     "has_fragman": True
#   },
#   {
#     "id": 2,
#     "title": "Jurassic Park",
#     "description": "A theme park showcasing genetically cloned dinosaurs turns into a fight for survival.",
#     "follow": 850,
#     "gener_id": 2,
#     "release": "1993-06-11",
#     "has_fragman": True
#   },
#   {
#     "id": 3,
#     "title": "The Shawshank Redemption",
#     "description": "Two imprisoned men bond over several years, finding solace and eventual redemption.",
#     "follow": 1200,
#     "gener_id": 3,
#     "release": "1994-09-23",
#     "has_fragman": False
#   },
#   {
#     "id": 4,
#     "title": "Inception",
#     "description": "A thief who steals corporate secrets through dream-sharing technology gets a complex task.",
#     "follow": 1350,
#     "gener_id": 4,
#     "release": "2010-07-16",
#     "has_fragman":True
#   },
#   {
#     "id": 5,
#     "title": "The Dark Knight",
#     "description": "Batman confronts the Joker, who brings chaos to Gotham City.",
#     "follow": 980,
#     "gener_id": 4,
#     "release": "2008-07-18",
#     "has_fragman":True
#   },
#   {
#     "id": 6,
#     "title": "Pulp Fiction",
#     "description": "Interconnected stories of criminals and lowlifes in Los Angeles.",
#     "follow": 750,
#     "gener_id": 5,
#     "release": "1994-10-14",
#     "has_fragman": True
#   },
#   {
#     "id": 7,
#     "title": "The Matrix",
#     "description": "A computer hacker learns about the True nature of his reality.",
#     "follow": 1050,
#     "gener_id": 4,
#     "release": "1999-03-31",
#     "has_fragman": False
#   },
#   {
#     "id": 8,
#     "title": "Forrest Gump",
#     "description": "A simple-minded but kind-hearted man witnesses and influences several historical events.",
#     "follow": 1150,
#     "gener_id": 3,
#     "release": "1994-07-06",
#     "has_fragman": True
#   },
#   {
#     "id": 9,
#     "title": "Star Wars: Episode IV - A New Hope",
#     "description": "Luke Skywalker begins a journey to become a Jedi and save the galaxy from the Empire.",
#     "follow": 1450,
#     "gener_id": 6,
#     "release": "1977-05-25",
#     "has_fragman": True
#   },
#   ]
# query="""
# INSERT INTO movie(title,description,follow,gener_id,release,has_fragman)
# VALUES (%s,%s,%s,%s,%s,%s)
# """
# for info in data:
#     cur.execute(query,(info['title'][:8],info['description'][:10],info['follow'],info['gener_id'],info['release'],info['has_fragman']))

# cur.execute("SELECT * FROM movie;")
# # print(cur.fetchall())
# # cur.execute(query)
# conn.commit()

##################   TASK 3   #########################


# one=psycopg2.connect('dbname=store user=postgres host=localhost port=5432 password=1997')
# zero=one.cursor()
# liste="""
# CREATE TABLE product(
# mehsul_id SERIAL PRIMARY KEY,
# mehsul_adi VARCHAR(50),
# mehsul_sayi INT DEFAULT 0,
# new_mehsul TEXT NOT NULL,
# mehsul_tarix DATE,
# mehsul_saat TIME,
# son_tarix DATE,
# qiymet INT NOT NULL,
# satisi INT DEFAULT 0,
# bar_kod VARCHAR(12) UNIQUE

# );

# """
# zero.execute(liste)
# data = [
#     {
#         "mehsul_id": 1,
#         "mehsul_adi": "Samsung Galaxy S21",
#         "mehsul_sayi": 100,
#         "new_mehsul": "Yes",
#         "mehsul_tarix": "2023-06-01",
#         "mehsul_saat": "10:00:00",
#         "son_tarix": "2023-06-30",
#         "qiymet": 1999,
#         "satisi": 50,
#         "bar_kod": "123456789012"
#     },
#     {
#         "mehsul_id": 2,
#         "mehsul_adi": "Apple iPhone 12",
#         "mehsul_sayi": 50,
#         "new_mehsul": "No",
#         "mehsul_tarix": "2023-05-15",
#         "mehsul_saat": "14:30:00",
#         "son_tarix": "2023-06-30",
#         "qiymet": 2499,
#         "satisi": 20,
#         "bar_kod": "234567890123"
#     },
#     {
#         "mehsul_id": 3,
#         "mehsul_adi": "Sony PlayStation 5",
#         "mehsul_sayi": 30,
#         "new_mehsul": "Yes",
#         "mehsul_tarix": "2023-05-10",
#         "mehsul_saat": "16:45:00",
#         "son_tarix": "2023-06-30",
#         "qiymet": 499,
#         "satisi": 10,
#         "bar_kod": "345678901234"
#     },
#     {
#         "mehsul_id": 4,
#         "mehsul_adi": "LG 55-Inch 4K Smart TV",
#         "mehsul_sayi": 20,
#         "new_mehsul": "No",
#         "mehsul_tarix": "2023-05-20",
#         "mehsul_saat": "12:15:00",
#         "son_tarix": "2023-06-30",
#         "qiymet": 799,
#         "satisi": 5,
#         "bar_kod": "456789012345"
#     },
#     {
#         "mehsul_id": 5,
#         "mehsul_adi": "Nike Air Max 270",
#         "mehsul_sayi": 80,
#         "new_mehsul": "Yes",
#         "mehsul_tarix": "2023-05-05",
#         "mehsul_saat": "09:30:00",
#         "son_tarix": "2023-06-30",
#         "qiymet": 129,
#         "satisi": 40,
#         "bar_kod": "567890123456"
#     },
# ]
# liste="""
# INSERT INTO product(mehsul_adi,mehsul_sayi,new_mehsul,mehsul_tarix,mehsul_saat,son_tarix,qiymet,satisi,bar_kod)
# VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
# """
# for info in data:
    
#   zero.execute(liste,(info['mehsul_adi'],info['mehsul_sayi'],info['new_mehsul'],info['mehsul_tarix'],info['mehsul_saat'],info['son_tarix'],info['qiymet'],info['satisi'],info['bar_kod'][:5]))
  
# one.commit()


########################## task4     #############################
one=psycopg2.connect('dbname=clinic user=postgres host=localhost port=5432 password=1997')

zero=one.cursor()

##############  1  #####################

# number="""
# CREATE TABLE sobe(
# sobe_id SERIAL PRIMARY KEY,
# sobe_title VARCHAR(20)
# )
# """
# zero.execute(number)
# data=[
# ('Stomatologiya',),
# ('Kardiologiya',),
# ('Urologiya',)
# ]
# number="""
# INSERT INTO sobe(sobe_title) 
# VALUES (%s)

# """
# for info in data:
#     zero.execute(number,info)

#########  2  ###############


# number = """
# CREATE TABLE doctor(
#     doctor_id SERIAL PRIMARY KEY,
#     doctor_title VARCHAR(20),
#     name_id INT,
#     CONSTRAINT blog_box 
#         FOREIGN KEY (name_id) 
#             REFERENCES sobe(sobe_id) 
#             ON DELETE SET NULL
# )
# """

# zero.execute(number)

# data=[
# ('Dr.Haciyev',1),
# ('Dr.Eliyeva',2),
# ('Dr.Axhmedov',3)

# ]
# number="""
# INSERT INTO doctor(doctor_title,name_id) VALUES (%s,%s)
# """
# for info in data:
#     zero.execute(number,info)

############  3  ############

# number = """
# CREATE TABLE article(
#     article_id SERIAL PRIMARY KEY,
#     article_title VARCHAR(25),
#     doctor_name INT,
#     CONSTRAINT article_box
#         FOREIGN KEY(doctor_name)
#             REFERENCES doctor(doctor_id)
#             ON DELETE SET NULL
# )
# """

# zero.execute(number)

# data=[
# ('dis xestelikleri',1),
# ('Infarkt nece yaranir',2),
# ('Boyrek dasinin mualicesi',3)
# ]
# number="""
# INSERT INTO article(article_title,doctor_name) VALUES (%s,%s)
# """
# for info in data:
#     zero.execute(number,info)

############## 4  #############
# number="""
# CREATE TABLE category(
# category_id SERIAL PRIMARY KEY,
# category_title VARCHAR(20),
# article_name INT
# );
# ALTER TABLE category
# ADD CONSTRAINT article_box
# FOREIGN KEY(article_name)
# REFERENCES article(article_id)
# ON DELETE SET NULL

# """
# zero.execute(number)
# data=[
# ('Ortodont',2),
# ('Kardiolog',3),
# ('Urolog',1)
# ]
# number="""
# INSERT INTO category(category_title,article_name) VALUES (%s,%s)
# """
# for info in data:
#     zero.execute(number,info)

##########################







one.commit()
