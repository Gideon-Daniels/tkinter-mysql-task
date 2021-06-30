class DatabaseHospital:
    def __init__(self):
        # Connecting to the database
        # importing 'mysql.connector' as mysql for convenient
        import mysql.connector as mysql
        # connecting to the database using 'connect()' method
        # it takes 3 required parameters 'host', 'user', 'passwd'
        self.db = mysql.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="Hospital"
        )
        # creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
        self.cursor = self.db.cursor()

    def select_username(self):
        # defining the Query
        query_user = "SELECT user FROM Login"
        # getting records from the table
        self.cursor.execute(query_user)
        # fetching all records from the 'cursor' object
        records = self.cursor.fetchall()
        # showing the data
        # for user in records:
        #     return user
        return records

    def select_password(self):
        query_password = "SELECT password FROM Login"
        self.cursor.execute(query_password)
        records = self.cursor.fetchall()
        # for password in records:
        #     return password
        return records

    def insert(self, user, password):
        pass


# username = DatabaseHospital().select_username()
# password = DatabaseHospital().select_password()
# entered_username = "Ashwin"
# print("USERNAMES :", username)
# print("PASSWORDS :", password)
#
# for x in range(len(username)):
#     # print(username[x])
#     if entered_username in username[x]:
#         print("CORRECT")
#         break
#     else:
#         print("Incorrect")
