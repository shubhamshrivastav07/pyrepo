


class User():
    fname=""
    lname=""
    
    def setFname(self,fname):
        self.fname=fname
    def getFname(self):
        return self.fname

    def setLname(self,lname):
        self.lname= lname
    
    def getLname(self):
        return self.lname


    def __dict__(self):
        return f" {self.fname}     {self.lname}"



