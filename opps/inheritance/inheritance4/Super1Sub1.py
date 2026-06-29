
from Sub1 import DbBase

class UserClass(DbBase):

    def userSave(self):
        print("User Save")


u=UserClass()
u.configurtion()
u.dbConfig()
u.dbConnect()
u.userSave()