
from MainBase import Base

class DbBase(Base):

    def dbConfig(self):
        print("Data Base Fonfig")
    
    def dbConnect(self):
        print("Data Base Connect")