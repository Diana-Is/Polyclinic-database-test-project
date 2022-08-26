from general_person import general_person

class  patient(general_person):
    def __init__(self, code,surname,name,otchestvo,year_of_birth):
        general_person.__init__(self,code,surname,name,otchestvo)
        self.setYear_of_birth(year_of_birth)

    def setYear_of_birth(self,value):self.__year_of_birth=value
    def getYear_of_birth(self):return self.__year_of_birth        

    def __str__(self):
        p="%s %s %s %s %s"%(self.getCode(),self.getSurname(),self.getName(),self.getOtchestvo(), self.getYear_of_birth())
        return p
    def getEntry(self):
        p="%s %s %s %s %s"%(self.getCode(),self.getSurname(),self.getName(),self.getOtchestvo(), self.getYear_of_birth())
        return p