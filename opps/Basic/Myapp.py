

from opps.Basic.Beans import User
from opps.Basic.Data import Data

class  MyApp():


    def __init__(self):
        u=User()
        u.setFname("raj")
        u.setLname("sharma")

        d= Data()
        d.DataReader(u.__dict__())



m= MyApp()
