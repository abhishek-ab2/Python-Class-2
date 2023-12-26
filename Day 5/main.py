class User:
    def __init__(self, name, age, dob='1-1-2000'):
        self.name = name
        self.age = age
        self.dob = dob
        self.is_stored_in_db = False

        # self.store_to_db()

    def store_to_db(self, **creds):
        print('Storing data to db....')
        self.is_stored_in_db = True

    # def __str__(self):
    #     return 'User object for ' + self.name

    # def __repr__(self):
    #     return 'User object'

    # def __del__(self):
    #     print('Deleting from db')


user1 = User('Abhishek', 400)
user2 = User('User 2', 9876, '1-1-98765')

# user1.store_to_db()
print(user1)

# print(user2.name, user2.age, user2.dob, user2.is_stored_in_db)



