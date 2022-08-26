from doctor import doctor
from patient import patient

class  appeal():
    def __init__(self,code,doctor1,patient1,date_of_application,diagnosis,price):
     self.setCode(code)
     if isinstance(doctor1,doctor):
        self.setDoctor(doctor1)
     else:
        raise Exception("Was not possible to create an object of class appeal because of wrong argument")
        #self.setDoctor(doctor(0,"surname_not_filled_in._wrong_input","name_not_filled_in._wrong_input","otch_not_filled_in._wrong_input","spez_not_filled_in._wrong_input","categ_not_filled_in._wrong_input"))
     if isinstance(patient1,patient):
        self.setPatient(patient1)
     else:
        raise Exception("Was not possible to create an object of class appeal because of wrong argument")
        self.setPatient(patient(0,"surname_not_filled_in._wrong_input","name_not_filled_in._wrong_input","otch_not_filled_in._wrong_input","birth_not_filled_in._wrong_input"))
     self.setDate_of_application(date_of_application)
     self.setDiagnosis(diagnosis)
     self.setPrice(price)
     
    def setCode(self,value):self.__code=value
    def getCode(self):return self.__code
     
    def setDoctor(self,value):self.__doctor=value
    def getDoctor(self):return self.__doctor
    
    def setPatient(self,value):self.__patient=value
    def getPatient(self):return self.__patient
        
    def setDate_of_application(self,value):self.__date_of_application=value
    def getDate_of_application(self):return self.__date_of_application
        
    def setDiagnosis(self,value):self.__diagnosis=value
    def getDiagnosis(self):return self.__diagnosis       

    def setPrice(self,value):self.__price=value
    def getPrice(self):return self.__price  


    def __str__(self):
        m="%s %s %s %s %s %s"%(self.getCode(),self.getDoctor(),self.getPatient(),self.getDate_of_application(), self.getDiagnosis(),self.getPrice())
        return m
    def getEntry(self):
        m="%s %s %s %s %s %s"%(self.getCode(),self.getDoctor(),self.getPatient(),self.getDate_of_application(), self.getDiagnosis(),self.getPrice())
        return m