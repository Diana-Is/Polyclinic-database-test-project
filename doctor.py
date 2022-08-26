#-*- coding:utf-8 -*-
from general_person import general_person

class  doctor(general_person):
    def __init__(self, code=0,surname="",name="",otchestvo="",specialization="",category=""):
        general_person.__init__(self,code,surname,name,otchestvo)
        self.setSpecialization(specialization)
        self.setCategory(category)
    def setSpecialization(self,value):self.__specialization=value
    def getSpecialization(self):return self.__specialization        
    def setCategory(self,value):self.__category=value
    def getCategory(self):return self.__category  
    def __str__(self):
        s="%s %s %s %s %s %s"%(self.getCode(),self.getSurname(),self.getName(),self.getOtchestvo(), self.getSpecialization(), self.getCategory())
        return s
    def getEntry(self):
        s="%s %s %s %s %s %s"%(self.getCode(),self.getSurname(),self.getName(),self.getOtchestvo(), self.getSpecialization(), self.getCategory())
        return s
