#-*- coding:utf-8 -*-
import os
import sqlite3 as db
from data import data

emptydb = """
PRAGMA foreign_keys = ON;

create table doctor
(code integer primary key,
surname text,
name text,
otchestvo text,
specialization text,
category text);

create table patient
(code integer primary key,
surname text,
name text,
otchestvo text,
year_of_birth text);

create table appeals
(code integer primary key,
doctor integer,
patient integer,
date_of_application text,
diagnosis text,
price integer);

"""

class datasql(data):
	def read(self):
		conn = db.connect(self.getInp())
		curs = conn.cursor()
		curs.execute('select code,surname,name,otchestvo,specialization,category from doctor')
		data=curs.fetchall()
		for r in data:self.getLib().newDoc(r[0],r[1],r[2],r[3],r[4],r[5])
		curs.execute('select code,surname,name,otchestvo,year_of_birth from patient')
		data=curs.fetchall()
		for r in data:self.getLib().newPat(r[0],r[1],r[2],r[3],r[4])
		curs.execute('select code,doctor,patient,date_of_application,diagnosis,price from appeals')
		data=curs.fetchall()
		for r in data:self.getLib().newApp(r[0],self.getLib().findDocByCode(int(r[1])),self.getLib().findPatByCode(int(r[2])),r[3],r[4],r[5])
		conn.close()
	def write(self):
		conn = db.connect(self.getOut())
		curs = conn.cursor()
		curs.executescript(emptydb)
		for c in self.getLib().getDocCodes():
			curs.execute("insert into doctor(code,surname,name,otchestvo,specialization,category) values('%s','%s','%s','%s','%s','%s')"%(str(c),
				self.getLib().getDocSurname(c),
				self.getLib().getDocName(c),
				self.getLib().getDocOtchestvo(c),
				self.getLib().getDocSpecialization(c),
				self.getLib().getDocCategory(c)))
		for c in self.getLib().getPatCodes():
			curs.execute("insert into patient(code,surname,name,otchestvo,year_of_birth) values('%s','%s','%s','%s','%s')"%(str(c),
				self.getLib().getPatSurname(c),self.getLib().getPatName(c),self.getLib().getPatOtchestvo(c),self.getLib().getPatYear_of_birth(c)))
		for c in self.getLib().getAppCodes():
		    curs.execute("insert into appeals(code,doctor,patient,date_of_application,diagnosis,price) values('%s','%s','%s','%s','%s','%s')"%( str(c),
			self.getLib().getAppDoctor(c).getCode(),
			self.getLib().getAppPatient(c).getCode(),
			self.getLib().getAppDate_of_application(c),
			self.getLib().getAppDiagnosis(c),
			self.getLib().getAppPrice(c)))
		conn.commit()
		conn.close()