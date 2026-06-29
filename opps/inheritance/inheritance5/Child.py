
from Sub1 import DbConfig
from Sub2 import Logger

class User(DbConfig,Logger):


    def userinfo(self):
        print("save user Info")



u= User()

u.config() # Base Parent
u.dbConfig() # Sub1 Parent
u.info() # Sub2 Parent2
u.userinfo() #main Child