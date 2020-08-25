# -*- coding: utf-8 -*-
"""
Created by Majd Barchini on 08/20/2020
"""

import sqlite3

def ConnectData():
    connect = sqlite3.connect("PatiantBook.db")
    cur = connect.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS PatiantBook (id INTEGER PRIMARY KEY, Name text, Sex_Combo text,
                Age text, Status_Combo text, Address text, Height text, Weight_Current text,
                Weight_Perfect text, Weight_Changed text, BMI text, Leather_tuck text, Arm_Circu text,
                Sick_Prev text, Sick_Curr text, Pressure text, Pulse text, Temperature text, Breath text,
                Urin_Exp text, Cyanosis text, Elevate text, Pallor text, Dryness text,
                Edema text, Hair text, Sleep text, Constipation text, Diarrhea text, Vomiting text,
                Urin_Color text, Urin_Number text, Current_sym1 text, Current_sym2 text, Current_sym3 text,
                Current_sym4 text, Uria text, Humo text, Krea text, Na text, K text, Ca text, WBC text,
                Pro text, Sug text, Beliro text, Fe text, Thyroid text, Urin_Acid text, Evaluation text,
                Start_Date text, Day_Combo text)""")
    connect.commit()
    connect.close()

def AddDataRec(Name, Sex_Combo, Age, Status_Combo, Address, Height, Weight_Current, Weight_Perfect,
               Weight_Changed, BMI, Leather_tuck, Arm_Circu, Sick_Prev, Sick_Curr, Pressure, Pulse,
               Temperature, Breath, Urin_Exp, Cyanosis, Elevate, Pallor, Dryness, Edema, Hair, Sleep,
               Constipation, Diarrhea, Vomiting, Urin_Color, Urin_Number, Current_sym1, Current_sym2,
               Current_sym3, Current_sym4, Uria, Humo, Krea, Na, K, Ca, WBC, Pro, Sug, Beliro,
               Fe, Thyroid, Urin_Acid, Evaluation, Start_Date, Day_Combo):
    
    connect = sqlite3.connect("PatiantBook.db")
    cur = connect.cursor()
    cur.execute("""INSERT INTO PatiantBook VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?,
                ?)""", (Name, Sex_Combo, Age, Status_Combo, Address, Height, Weight_Current, Weight_Perfect,
                Weight_Changed, BMI, Leather_tuck, Arm_Circu, Sick_Prev, Sick_Curr, Pressure, Pulse,
                Temperature, Breath, Urin_Exp, Cyanosis, Elevate, Pallor, Dryness, Edema, Hair, Sleep,
                Constipation, Diarrhea, Vomiting, Urin_Color, Urin_Number, Current_sym1, Current_sym2,
                Current_sym3, Current_sym4, Uria, Humo, Krea, Na, K, Ca, WBC, Pro, Sug, Beliro, Fe, Thyroid,
                Urin_Acid, Evaluation, Start_Date, Day_Combo))

    connect.commit()
    connect.close()
    
def ShowDataRec():
    connect = sqlite3.connect("PatiantBook.db")
    cur = connect.cursor()
    cur.execute("SELECT * FROM PatiantBook")
    rows = cur.fetchall()
    connect.close()
    
    return rows
    
def ShowPatiantRec(Patiant):
    connect = sqlite3.connect("PatiantBook.db")
    cur = connect.cursor()
    cur.execute("SELECT * FROM PatiantBook WHERE Name = ?", (Patiant,))
    row = cur.fetchall()
    connect.close()
    
    return row
    

def DeletePatiantRec(Patiant):
    connect = sqlite3.connect("PatiantBook.db")
    cur = connect.cursor()
    cur.execute("DELETE FROM PatiantBook WHERE Name = ?", (Patiant,))
    connect.commit()
    connect.close()

def UpdatePatiantRec(ID, Name, Sex_Combo, Age, Status_Combo, Address, Height, Weight_Current, Weight_Perfect,
               Weight_Changed, BMI, Leather_tuck, Arm_Circu, Sick_Prev, Sick_Curr, Pressure, Pulse,
               Temperature, Breath, Urin_Exp, Cyanosis, Elevate, Pallor, Dryness, Edema, Hair, Sleep,
               Constipation, Diarrhea, Vomiting, Urin_Color, Urin_Number, Current_sym1, Current_sym2,
               Current_sym3, Current_sym4, Uria, Humo, Krea, Na, K, Ca, WBC, Pro, Sug, Beliro,
               Fe, Thyroid, Urin_Acid, Evaluation, Start_Date, Day_Combo):

    connect = sqlite3.connect("PatiantBook.db")
    cur = connect.cursor()
    cur.execute("""UPDATE PatiantBook SET Name = ?, Sex_Combo = ?, Age = ?, Status_Combo = ?, Address = ?,
                Height = ?, Weight_Current = ?, Weight_Perfect = ?, Weight_Changed = ?, BMI = ?, Leather_tuck = ?,
                Arm_Circu = ?, Sick_Prev = ?, Sick_Curr = ?, Pressure = ?, Pulse = ?, Temperature = ?, Breath = ?,
                Urin_Exp = ?, Cyanosis = ?, Elevate = ?, Pallor = ?, Dryness = ?, Edema = ?, Hair = ?, Sleep = ?,
                Constipation = ?, Diarrhea = ?, Vomiting = ?, Urin_Color = ?, Urin_Number = ?, Current_sym1 = ?,
                Current_sym2 = ?, Current_sym3 = ?, Current_sym4 = ?, Uria = ?, Humo = ?, Krea = ?, Na = ?, K = ?,
                Ca = ?, WBC = ?, Pro = ?, Sug = ?, Beliro = ?, Fe = ?, Thyroid = ?, Urin_Acid = ?, Evaluation = ?,
                Start_Date = ?, Day_Combo = ? WHERE ID = ?""", (Name, Sex_Combo, Age, Status_Combo, Address,
                Height, Weight_Current, Weight_Perfect, Weight_Changed, BMI, Leather_tuck, Arm_Circu, Sick_Prev,
                Sick_Curr, Pressure, Pulse, Temperature, Breath, Urin_Exp, Cyanosis, Elevate, Pallor, Dryness,
                Edema, Hair, Sleep, Constipation, Diarrhea, Vomiting, Urin_Color, Urin_Number, Current_sym1,
                Current_sym2, Current_sym3, Current_sym4, Uria, Humo, Krea, Na, K, Ca, WBC, Pro, Sug, Beliro, Fe,
                Thyroid, Urin_Acid, Evaluation, Start_Date, Day_Combo, int(ID)))

    connect.commit()
    connect.close()

def ScheduleRec():
    connect = sqlite3.connect("PatiantBook.db")
    cur = connect.cursor()
    cur.execute("SELECT ID, Name, Day_Combo FROM PatiantBook")
    rows = cur.fetchall()
    connect.close()
    
    return rows

ConnectData()