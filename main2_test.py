#var1-----------------------------------
from polyclinic import polyclinic 
from dataxml import dataxml

polcl1=polyclinic()
dat1=dataxml(polcl1,'old.xml','new.xml')
dat1.read()

polcl1.removeDoctor(1)
polcl1.removeDoctor(4)
polcl1.removePatient(1)
polcl1.removePatient(4)
dat1.setOut('delete.xml') #resetting output file. like this it is more lakonichno.(look at functions in file data.py) 
dat1.write()

polcl1.clear()
dat1.setInp('delete.xml')#setting input file. 
dat1.setOut('new.xml') #resetting output file again. 
dat1.read()


for k in polcl1.getDocCodes():
    print(polcl1.findDocByCode(k)) 
    print(polcl1.getDocSurname(k)) 

dat1.write()

#for k in polcl1.getPatCodes():
    #print(polcl1.findPatByCode(k)) 
    #print(polcl1.getPatSurname(k))    

