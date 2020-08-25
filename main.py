# -*- coding: utf-8 -*-

"""
Created by Majd Barchini on 08/20/2020
"""

import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk
from datetime import datetime
import sys
from PIL import ImageTk, Image
import cv2
import database
from win10toast import ToastNotifier
from os import path

class MainDisplay(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.master = master

        self.menubar = Menu(self)
        self.master.config(menu = self.menubar)

        ##############################Variables###############################
        #Fonts
        self.font_title = ('arial', 12, 'bold')
        self.font_text = ("arial", 8)
        
        #Dates
        self.Start_Date = tk.StringVar()
        self.Notification_date = tk.StringVar()
        
        #Personal Info
        self.Name = tk.StringVar()
        self.Sex = tk.StringVar()
        self.Age = tk.StringVar()
        self.Status = tk.StringVar()
        self.Address = tk.StringVar()
        
        #Measurements
        self.Height = tk.StringVar()
        self.Weight_Current = tk.StringVar()
        self.Weight_Perfect = tk.StringVar()
        self.Weight_Changed = tk.StringVar()
        self.BMI = tk.StringVar()
        self.Leather_tuck = tk.StringVar()
        self.Arm_Circu = tk.StringVar()
        
        #Sickness
        self.Sick_Prev = tk.StringVar()
        self.Sick_Curr = tk.StringVar()
        
        #BioInfo
        self.Pressure = tk.StringVar()
        self.Pulse = tk.StringVar()
        self.Temperature = tk.StringVar()
        self.Breath = tk.StringVar()
        self.Urin_Exp = tk.StringVar()
        
        #Meditation
        self.Cyanosis = tk.StringVar()
        self.Elevate = tk.StringVar()
        self.Pallor = tk.StringVar()
        self.Dryness = tk.StringVar()
        self.Edema = tk.StringVar()
        self.Hair = tk.StringVar()
        
        #Changes
        self.Sleep = tk.StringVar()
        self.Constipation = tk.StringVar()
        self.Diarrhea = tk.StringVar()
        self.Vomiting = tk.StringVar()
        self.Urin_Color = tk.StringVar()
        self.Urin_Number = tk.StringVar()
        
        #Current_sym
        self.Current_sym1 = tk.StringVar()
        self.Current_sym2 = tk.StringVar()
        self.Current_sym3 = tk.StringVar()
        self.Current_sym4 = tk.StringVar()
        
        #Special Cases
        ##Lab Test
        self.Uria = tk.StringVar()
        self.Humo = tk.StringVar()
        self.Krea = tk.StringVar()
        self.Na = tk.StringVar()
        self.K = tk.StringVar()
        self.Ca = tk.StringVar()
        self.WBC = tk.StringVar()
        self.Pro = tk.StringVar()
        self.Sug = tk.StringVar()
        
        ##Extra test
        self.Beliro = tk.StringVar()
        self.Fe = tk.StringVar()
        self.Thyroid = tk.StringVar()
        self.Urin_Acid = tk.StringVar()
        
        ##Evaluation
        self.Evaluation = tk.StringVar()

        ################################Clock#################################
        self.ClockFrame = tk.Frame(self.master, width = 1350, height = 50, bd = 5, relief = "ridge")
        self.ClockFrame.pack(side = "bottom", fill = "x", expand = 1, anchor = 's')
        self.Time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.ClockLabel = tk.Label(self.ClockFrame, text = self.Time, anchor = 'e')
        self.ClockLabel.pack(side = 'right')
        self.Clock()

        ##############################Main Frame###############################
        self.MainFrame = tk.Frame(self.master, relief = 'ridge')
        self.MainFrame.pack(side = "top", fill = "x", expand = 1, anchor = 'n')

        self.RightFrame = tk.Frame(self.MainFrame, height = height, width = width, relief = 'ridge')
        self.RightFrame.grid(row=0, column=1, sticky = "news")
        
        ##############################Buttons Frame###############################
        self.ButtonFrame = tk.Frame(self.RightFrame, height = height, width = width, relief = 'ridge')
        self.ButtonFrame.grid(row = 0, column = 0, columnspan = 10)
        
        self.Add_Button = tk.Button(self.ButtonFrame, font = self.font_text, text = "Add New", padx = 4, pady = 4, width = 15, command = self.AddData)
        self.Add_Button.grid(row = 0, column = 0)
        
        self.Clear_Button = tk.Button(self.ButtonFrame, font = self.font_text, text = "Clear", padx = 4, pady = 4, width = 15, command = self.Clear)
        self.Clear_Button.grid(row = 0, column = 1)
        
        self.Delete_Button = tk.Button(self.ButtonFrame, font = self.font_text, text = "Delete", padx = 4, pady = 4, width = 15, command = self.DeletePatiant)
        self.Delete_Button.grid(row = 0, column = 2)
        
        self.Update_Button = tk.Button(self.ButtonFrame, font = self.font_text, text = "Update", padx = 4, pady = 4, width = 15, command = self.UpdatePatiant)
        self.Update_Button.grid(row = 0, column = 3)
        
        self.Exit_Button = tk.Button(self.ButtonFrame, font = self.font_text, text = "Exit", padx = 4, pady = 4, width = 15, command = self.on_exit)
        self.Exit_Button.grid(row = 0, column = 4)
        
        ##############################Personal Info###############################
        self.Personal_info = tk.Label(self.RightFrame, font = self.font_title, text = "Personal Information", padx = 4, pady = 4)
        self.Personal_info.grid(row = 1, column = 0, columnspan = 10, sticky = "w")

        self.FullName_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Full Name", padx = 4, pady = 4)
        self.FullName_Label.grid(row = 2, column = 0, sticky = "ew")
        self.FullName_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Name, width = 20)
        self.FullName_Entry.grid(row = 2, column = 1, columnspan = 2, sticky = "ew")
        
        self.Sex_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Sex", padx = 4, pady = 4)
        self.Sex_Label.grid(row = 2, column = 2, sticky = "nswe")
        self.Sex_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Sex, width = 10)
        self.Sex_Entry.grid(row = 2, column = 3, sticky = "ew")
        
        self.Age_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Age", padx = 4, pady = 4)
        self.Age_Label.grid(row = 2, column = 4, sticky = "ew")
        self.Age_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Age, width = 15)
        self.Age_Entry.grid(row = 2, column = 5, sticky = "ew")
        
        self.Status_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Status", padx = 4, pady = 4)
        self.Status_Label.grid(row = 2, column = 6, sticky = "ew")
        self.Status_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Status, width = 10)
        self.Status_Entry.grid(row = 2, column = 7, sticky = "ew")
        
        self.Address_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Address", padx = 4, pady = 4)
        self.Address_Label.grid(row = 2, column = 8, sticky = "ew")
        self.Address_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Address, width = 15)
        self.Address_Entry.grid(row = 2, column = 9, columnspan = 2, sticky = "ew")

        ##############################Measurement Info###############################
        self.Measurement_info = tk.Label(self.RightFrame, font = self.font_title, text = "Measurement Information", padx = 4, pady = 4)
        self.Measurement_info.grid(row = 3, column = 0, columnspan = 10, sticky = "w")

        self.Height_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Height", padx = 4, pady = 4)
        self.Height_Label.grid(row = 4, column = 0, sticky = "ew")
        self.Height_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Height, width = 10)
        self.Height_Entry.grid(row = 4, column = 1, sticky = "ew")
        
        self.C_Weight_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Current Weight", padx = 4, pady = 4)
        self.C_Weight_Label.grid(row = 4, column = 2, sticky = "ew")
        self.C_Weight_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Weight_Current, width = 10)
        self.C_Weight_Entry.grid(row = 4, column = 3, sticky = "ew")
        
        self.P_Weight_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Perfect Weight", padx = 4, pady = 4)
        self.P_Weight_Label.grid(row = 4, column = 4, sticky = "ew")
        self.P_Weight_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Weight_Perfect, width = 10)
        self.P_Weight_Entry.grid(row = 4, column = 5, sticky = "ew")
        
        self.Changed_Weight_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Changed Weight", padx = 4, pady = 4)
        self.Changed_Weight_Label.grid(row = 4, column = 6, sticky = "ew")
        self.Changed_Weight_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Weight_Changed, width = 10)
        self.Changed_Weight_Entry.grid(row = 4, column = 7, sticky = "ew")
        
        self.BMI_Label = tk.Label(self.RightFrame, font = self.font_text, text = "BMI", padx = 4, pady = 4)
        self.BMI_Label.grid(row = 4, column = 8, sticky = "ew")
        self.BMI_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.BMI, width = 15)
        self.BMI_Entry.grid(row = 4, column = 9, sticky = "ew")
        
        self.Leather_tuck_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Leather Tuck", padx = 4, pady = 4)
        self.Leather_tuck_Label.grid(row = 5, column = 0, sticky = "ew")
        self.Leather_tuck_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Leather_tuck, width = 10)
        self.Leather_tuck_Entry.grid(row = 5, column = 1, sticky = "ew")
        
        self.Arm_Circu_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Arm Circumference", padx = 4, pady = 4)
        self.Arm_Circu_Label.grid(row = 5, column = 2, sticky = "ew")
        self.Arm_Circu_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Arm_Circu, width = 10)
        self.Arm_Circu_Entry.grid(row = 5, column = 3, sticky = "ew")
        
        ##############################Sickness Info###############################
        self.Sickness_info = tk.Label(self.RightFrame, font = self.font_title, text = "Sickness Information", padx = 4, pady = 4)
        self.Sickness_info.grid(row = 6, column = 0, columnspan = 10, sticky = "w")
        
        self.Sick_Prev_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Previous Sickness", padx = 4, pady = 4)
        self.Sick_Prev_Label.grid(row = 7, column = 0, sticky = "ew")
        self.Sick_Prev_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Sick_Prev, width = 10)
        self.Sick_Prev_Entry.grid(row = 7, column = 1, columnspan = 9, sticky = "ew")
        
        self.Sick_Curr_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Current Sickness", padx = 4, pady = 4)
        self.Sick_Curr_Label.grid(row = 8, column = 0, sticky = "ew")
        self.Sick_Curr_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Sick_Curr, width = 10)
        self.Sick_Curr_Entry.grid(row = 8, column = 1, columnspan = 9, sticky = "ew")
        
        ##############################Vital Signal###############################
        self.VitalSignal_info = tk.Label(self.RightFrame, font = self.font_title, text = "Vital Signals", padx = 4, pady = 4)
        self.VitalSignal_info.grid(row = 9, column = 0, columnspan = 10, sticky = "w")
        
        self.Pressure_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Blood Pressure", padx = 4, pady = 4)
        self.Pressure_Label.grid(row = 10, column = 0, sticky = "ew")
        self.Pressure_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Pressure, width = 10)
        self.Pressure_Entry.grid(row = 10, column = 1, sticky = "ew")
        
        self.Pulse_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Pulse", padx = 4, pady = 4)
        self.Pulse_Label.grid(row = 10, column = 2, sticky = "ew")
        self.Pulse_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Pulse, width = 10)
        self.Pulse_Entry.grid(row = 10, column = 3, sticky = "ew")
        
        self.Temperature_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Temperature", padx = 4, pady = 4)
        self.Temperature_Label.grid(row = 10, column = 4, sticky = "ew")
        self.Temperature_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Temperature, width = 10)
        self.Temperature_Entry.grid(row = 10, column = 5, sticky = "ew")
        
        self.Breath_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Breath", padx = 4, pady = 4)
        self.Breath_Label.grid(row = 10, column = 6, sticky = "ew")
        self.Breath_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Breath, width = 10)
        self.Breath_Entry.grid(row = 10, column = 7, sticky = "ew")
        
        self.Urin_Exp_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Urine/day", padx = 4, pady = 4)
        self.Urin_Exp_Label.grid(row = 10, column = 8, sticky = "ew")
        self.Urin_Exp_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Urin_Exp, width = 15)
        self.Urin_Exp_Entry.grid(row = 10, column = 9, sticky = "ew")
        
        ##############################Meditation###############################
        self.Meditation = tk.Label(self.RightFrame, font = self.font_title, text = "Meditation", padx = 4, pady = 4)
        self.Meditation.grid(row = 11, column = 0, columnspan = 10, sticky = "w")
        
        self.Cyanosis_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Cyanosis", padx = 4, pady = 4)
        self.Cyanosis_Label.grid(row = 12, column = 0, sticky = "ew")
        self.Cyanosis_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Cyanosis, width = 10)
        self.Cyanosis_Entry.grid(row = 12, column = 1, sticky = "ew")
        
        self.Elevate_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Elevate", padx = 4, pady = 4)
        self.Elevate_Label.grid(row = 12, column = 2, sticky = "ew")
        self.Elevate_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Elevate, width = 10)
        self.Elevate_Entry.grid(row = 12, column = 3, sticky = "ew")
        
        self.Pallor_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Pallor", padx = 4, pady = 4)
        self.Pallor_Label.grid(row = 12, column = 4, sticky = "ew")
        self.Pallor_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Pallor, width = 10)
        self.Pallor_Entry.grid(row = 12, column = 5, sticky = "ew")
        
        self.Dryness_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Dryness", padx = 4, pady = 4)
        self.Dryness_Label.grid(row = 12, column = 6, sticky = "ew")
        self.Dryness_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Dryness, width = 10)
        self.Dryness_Entry.grid(row = 12, column = 7, sticky = "ew")
        
        self.Edema_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Edema", padx = 4, pady = 4)
        self.Edema_Label.grid(row = 12, column = 8, sticky = "ew")
        self.Edema_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Edema, width = 15)
        self.Edema_Entry.grid(row = 12, column = 9, sticky = "ew")
        
        self.Hair_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Hair", padx = 4, pady = 4)
        self.Hair_Label.grid(row = 12, column = 10, sticky = "ew")
        self.Hair_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Hair, width = 15)
        self.Hair_Entry.grid(row = 12, column = 11, sticky = "ew")
        
        ##############################Changes###############################
        self.Changes = tk.Label(self.RightFrame, font = self.font_title, text = "Changes", padx = 4, pady = 4)
        self.Changes.grid(row = 13, column = 0, columnspan = 10, sticky = "w")
        
        self.Sleep_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Sleep", padx = 4, pady = 4)
        self.Sleep_Label.grid(row = 14, column = 0, sticky = "ew")
        self.Sleep_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Sleep, width = 10)
        self.Sleep_Entry.grid(row = 14, column = 1, sticky = "ew")
        
        self.Constipation_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Constipation", padx = 4, pady = 4)
        self.Constipation_Label.grid(row = 14, column = 2, sticky = "ew")
        self.Constipation_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Constipation, width = 10)
        self.Constipation_Entry.grid(row = 14, column = 3, sticky = "ew")
        
        self.Diarrhea_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Diarrhea", padx = 4, pady = 4)
        self.Diarrhea_Label.grid(row = 14, column = 4, sticky = "ew")
        self.Diarrhea_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Diarrhea, width = 10)
        self.Diarrhea_Entry.grid(row = 14, column = 5, sticky = "ew")
        
        self.Vomiting_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Vomiting", padx = 4, pady = 4)
        self.Vomiting_Label.grid(row = 14, column = 6, sticky = "ew")
        self.Vomiting_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Vomiting, width = 10)
        self.Vomiting_Entry.grid(row = 14, column = 7, sticky = "ew")
        
        self.Urin_Color_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Urine Color", padx = 4, pady = 4)
        self.Urin_Color_Label.grid(row = 14, column = 8, sticky = "ew")
        self.Urin_Color_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Urin_Color, width = 15)
        self.Urin_Color_Entry.grid(row = 14, column = 9, sticky = "ew")
        
        self.Urin_Number_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Urine Number", padx = 4, pady = 4)
        self.Urin_Number_Label.grid(row = 14, column = 10, sticky = "ew")
        self.Urin_Number_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Urin_Number, width = 15)
        self.Urin_Number_Entry.grid(row = 14, column = 11, sticky = "ew")
        
        ##############################Symptoms###############################
        self.Symptoms = tk.Label(self.RightFrame, font = self.font_title, text = "Current Symptoms", padx = 4, pady = 4)
        self.Symptoms.grid(row = 15, column = 0, columnspan = 10, sticky = "w")
        
        self.Current_sym1_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Current_sym1, width = 15)
        self.Current_sym1_Entry.grid(row = 16, column = 1, columnspan = 4, sticky = "ew")
        
        self.Current_sym2_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Current_sym2, width = 15)
        self.Current_sym2_Entry.grid(row = 16, column = 5, columnspan = 4, sticky = "ew")
        
        self.Current_sym3_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Current_sym3, width = 15)
        self.Current_sym3_Entry.grid(row = 17, column = 1, columnspan = 4, sticky = "ew")
        
        self.Current_sym4_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Current_sym4, width = 15)
        self.Current_sym4_Entry.grid(row = 17, column = 5, columnspan = 4, sticky = "ew")
        
        ##############################Special Cases###############################
        self.Special = tk.Label(self.RightFrame, font = self.font_title, text = "Special Cases", padx = 4, pady = 4)
        self.Special.grid(row = 18, column = 0, columnspan = 10, sticky = "w")
        
        self.Lab = tk.Label(self.RightFrame, font = self.font_title, text = "* Lab Tests", padx = 4, pady = 4)
        self.Lab.grid(row = 19, column = 0, columnspan = 10, sticky = "w")
        
        self.Uria_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Uria", padx = 4, pady = 4)
        self.Uria_Label.grid(row = 20, column = 0, sticky = "ew")
        self.Uria_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Uria, width = 10)
        self.Uria_Entry.grid(row = 20, column = 1, sticky = "ew")
        
        self.Humo_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Humo", padx = 4, pady = 4)
        self.Humo_Label.grid(row = 20, column = 2, sticky = "ew")
        self.Humo_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Humo, width = 10)
        self.Humo_Entry.grid(row = 20, column = 3, sticky = "ew")
        
        self.Krea_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Krea", padx = 4, pady = 4)
        self.Krea_Label.grid(row = 20, column = 4, sticky = "ew")
        self.Krea_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Krea, width = 10)
        self.Krea_Entry.grid(row = 20, column = 5, sticky = "ew")
        
        self.Na_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Na", padx = 4, pady = 4)
        self.Na_Label.grid(row = 20, column = 6, sticky = "ew")
        self.Na_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Na, width = 10)
        self.Na_Entry.grid(row = 20, column = 7, sticky = "ew")
        
        self.K_Label = tk.Label(self.RightFrame, font = self.font_text, text = "K", padx = 4, pady = 4)
        self.K_Label.grid(row = 20, column = 8, sticky = "ew")
        self.K_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.K, width = 15)
        self.K_Entry.grid(row = 20, column = 9, sticky = "ew")
        
        self.Ca_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Ca", padx = 4, pady = 4)
        self.Ca_Label.grid(row = 21, column = 0, sticky = "ew")
        self.Ca_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Ca, width = 15)
        self.Ca_Entry.grid(row = 21, column = 1, sticky = "ew")
        
        self.WBC_Label = tk.Label(self.RightFrame, font = self.font_text, text = "W.B.C", padx = 4, pady = 4)
        self.WBC_Label.grid(row = 21, column = 2, sticky = "ew")
        self.WBC_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.WBC, width = 15)
        self.WBC_Entry.grid(row = 21, column = 3, sticky = "ew")
        
        self.Pro_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Pro", padx = 4, pady = 4)
        self.Pro_Label.grid(row = 21, column = 4, sticky = "ew")
        self.Pro_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Pro, width = 15)
        self.Pro_Entry.grid(row = 21, column = 5, sticky = "ew")
        
        self.Sug_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Sugar", padx = 4, pady = 4)
        self.Sug_Label.grid(row = 21, column = 6, sticky = "ew")
        self.Sug_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Sug, width = 15)
        self.Sug_Entry.grid(row = 21, column = 7, sticky = "ew")
        
        self.Lab = tk.Label(self.RightFrame, font = self.font_title, text = "* Extra Lab Tests", padx = 4, pady = 4)
        self.Lab.grid(row = 22, column = 0, columnspan = 10, sticky = "w")
        
        self.Beliro_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Beliro", padx = 4, pady = 4)
        self.Beliro_Label.grid(row = 23, column = 0, sticky = "ew")
        self.Beliro_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Beliro, width = 10)
        self.Beliro_Entry.grid(row = 23, column = 1, sticky = "ew")
        
        self.Fe_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Fe", padx = 4, pady = 4)
        self.Fe_Label.grid(row = 23, column = 2, sticky = "ew")
        self.Fe_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Fe, width = 10)
        self.Fe_Entry.grid(row = 23, column = 3, sticky = "ew")
        
        self.Thyroid_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Thyroid", padx = 4, pady = 4)
        self.Thyroid_Label.grid(row = 23, column = 0, sticky = "ew")
        self.Thyroid_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Thyroid, width = 10)
        self.Thyroid_Entry.grid(row = 23, column = 1, sticky = "ew")
        
        self.Urin_Acid_Label = tk.Label(self.RightFrame, font = self.font_text, text = "Urin Acid", padx = 4, pady = 4)
        self.Urin_Acid_Label.grid(row = 23, column = 2, sticky = "ew")
        self.Urin_Acid_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Urin_Acid, width = 10)
        self.Urin_Acid_Entry.grid(row = 23, column = 3, sticky = "ew")
        
        ##############################Evaluation###############################
        self.Evaluation_Label = tk.Label(self.RightFrame, font = self.font_title, text = "Evaluation", padx = 4, pady = 4)
        self.Evaluation_Label.grid(row = 24, column = 0, columnspan = 10, sticky = "w")
        
        self.Evaluation_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Evaluation, width = 10)
        self.Evaluation_Entry.grid(row = 24, column = 1, columnspan = 8, sticky = "ew")
        
        self.StartDate_Label = tk.Label(self.RightFrame, font = self.font_title, text = "Start Date:", padx = 4, pady = 4)
        self.StartDate_Label.grid(row = 25, column = 0)
        self.StartDate_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Start_Date, width = 10)
        self.StartDate_Entry.grid(row = 25, column = 1, sticky = "ew")
        
        self.Notification_Label = tk.Label(self.RightFrame, font = self.font_title, text = "Notification Date:", padx = 4, pady = 4)
        self.Notification_Label.grid(row = 25, column = 2, sticky = 'w')
        self.Notification_Entry = tk.Entry(self.RightFrame, font = self.font_text, textvariable = self.Notification_date, width = 10)
        self.Notification_Entry.grid(row = 25, column = 3, sticky = "w")
        
        #############################################################
        self.LeftFrame = tk.LabelFrame(self.MainFrame, height = height, relief = "solid", text = 'Patiant List')
        self.LeftFrame.grid(row=0, column=0, sticky = "news")
        
        self.scrollbar = ttk.Scrollbar(self.LeftFrame)
        self.scrollbar.grid(row = 0, column = 0, sticky = 'ns')
        
        self.PatiantList = tk.Listbox(self.LeftFrame, width = 50, height = height, bd = 5, font = self.font_text, yscrollcommand = self.scrollbar.set)
        self.PatiantList.bind('<<ListboxSelect>>', self.ShowPatiant)
        self.PatiantList.grid(row = 0, column = 1)
        
        self.scrollbar.config(command = self.PatiantList.yview)
        
        self.ShowData()
        self.Schedule()

    def Clock(self): 
        self.Time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.ClockLabel.configure(text = self.Time)
        self.master.after(1000, self.Clock)
    
    def Clear(self):
        self.Clear_conf = messagebox.askyesno("Rza's Nutrtion Software", "Confirm if you want to clear all data")
        if self.Clear_conf > 0:
            self.ClearData()
        
    def ClearData(self):
        self.Name.set("")
        self.Sex.set("")
        self.Age.set("")
        self.Status.set("")
        self.Address.set("")
        self.Height.set("")
        self.Weight_Current.set("")
        self.Weight_Perfect.set("")
        self.Weight_Changed.set("")
        self.BMI.set("")
        self.Leather_tuck.set("")
        self.Arm_Circu.set("")
        self.Sick_Prev.set("")
        self.Sick_Curr.set("")
        self.Pressure.set("")
        self.Pulse.set("")
        self.Temperature.set("")
        self.Breath.set("")
        self.Urin_Exp.set("")
        self.Cyanosis.set("")
        self.Elevate.set("")
        self.Pallor.set("")
        self.Dryness.set("")
        self.Edema.set("")
        self.Hair.set("")
        self.Sleep.set("")
        self.Constipation.set("")
        self.Diarrhea.set("")
        self.Vomiting.set("")
        self.Urin_Color.set("")
        self.Urin_Number.set("")
        self.Current_sym1.set("")
        self.Current_sym2.set("")
        self.Current_sym3.set("")
        self.Current_sym4.set("")
        self.Uria.set("")
        self.Humo.set("")
        self.Krea.set("")
        self.Na.set("")
        self.K.set("")
        self.Ca.set("")
        self.WBC.set("")
        self.Pro.set("")
        self.Sug.set("")
        self.Beliro.set("")
        self.Fe.set("")
        self.Thyroid.set("")
        self.Urin_Acid.set("")
        self.Evaluation.set("")
        self.Start_Date.set("")
        self.Notification_date.set("")
        
    def AddData(self):
        if self.Name.get():
            database.AddDataRec(self.Name.get(), self.Sex.get(), self.Age.get(), self.Status.get(),self.Address.get(),
                                 self.Height.get(), self.Weight_Current.get(), self.Weight_Perfect.get(), 
                                 self.Weight_Changed.get(), self.BMI.get(), self.Leather_tuck.get(), self.Arm_Circu.get(),
                                 self.Sick_Prev.get(), self.Sick_Curr.get(), self.Pressure.get(), self.Pulse.get(),
                                 self.Temperature.get(), self.Breath.get(),  self.Urin_Exp.get(), self.Cyanosis.get(), 
                                 self.Elevate.get(), self.Pallor.get(), self.Dryness.get(), self.Edema.get(), self.Hair.get(),
                                 self.Sleep.get(), self.Constipation.get(), self.Diarrhea.get(), self.Vomiting.get(),
                                 self.Urin_Color.get(), self.Urin_Number.get(), self.Current_sym1.get(), self.Current_sym2.get(),
                                 self.Current_sym3.get(), self.Current_sym4.get(), self.Uria.get(), self.Humo.get(),
                                 self.Krea.get(), self.Na.get(), self.K.get(), self.Ca.get(), self.WBC.get(), self.Pro.get(),
                                 self.Sug.get(), self.Beliro.get(), self.Fe.get(), self.Thyroid.get(), self.Urin_Acid.get(),
                                 self.Evaluation.get(), self.Start_Date.get(), self.Notification_date.get())
            self.ShowData()
            self.ClearData()
    
    def ShowData(self):
        self.PatiantList.delete(0, 'end')
        for row in database.ShowDataRec():
            self.name = row[1]
            self.PatiantList.insert('end', self.name)

    def ShowPatiant(self, event):
        self.SearchPatiant = self.PatiantList.curselection()[0]
        self.SelectPatiant = self.PatiantList.get(self.SearchPatiant)
        self.SelectedPatiant = database.ShowPatiantRec(self.SelectPatiant)[0]
        
        self.Name.set(self.SelectedPatiant[1])
        self.Sex.set(self.SelectedPatiant[2])
        self.Age.set(self.SelectedPatiant[3])
        self.Status.set(self.SelectedPatiant[4])
        self.Address.set(self.SelectedPatiant[5])
        self.Height.set(self.SelectedPatiant[6])
        self.Weight_Current.set(self.SelectedPatiant[7])
        self.Weight_Perfect.set(self.SelectedPatiant[8])
        self.Weight_Changed.set(self.SelectedPatiant[9])
        self.BMI.set(self.SelectedPatiant[10])
        self.Leather_tuck.set(self.SelectedPatiant[11])
        self.Arm_Circu.set(self.SelectedPatiant[12])
        self.Sick_Prev.set(self.SelectedPatiant[13])
        self.Sick_Curr.set(self.SelectedPatiant[14])
        self.Pressure.set(self.SelectedPatiant[15])
        self.Pulse.set(self.SelectedPatiant[16])
        self.Temperature.set(self.SelectedPatiant[17])
        self.Breath.set(self.SelectedPatiant[18])
        self.Urin_Exp.set(self.SelectedPatiant[19])
        self.Cyanosis.set(self.SelectedPatiant[20])
        self.Elevate.set(self.SelectedPatiant[21])
        self.Pallor.set(self.SelectedPatiant[22])
        self.Dryness.set(self.SelectedPatiant[23])
        self.Edema.set(self.SelectedPatiant[24])
        self.Hair.set(self.SelectedPatiant[25])
        self.Sleep.set(self.SelectedPatiant[26])
        self.Constipation.set(self.SelectedPatiant[27])
        self.Diarrhea.set(self.SelectedPatiant[28])
        self.Vomiting.set(self.SelectedPatiant[29])
        self.Urin_Color.set(self.SelectedPatiant[30])
        self.Urin_Number.set(self.SelectedPatiant[31])
        self.Current_sym1.set(self.SelectedPatiant[32])
        self.Current_sym2.set(self.SelectedPatiant[33])
        self.Current_sym3.set(self.SelectedPatiant[34])
        self.Current_sym4.set(self.SelectedPatiant[35])
        self.Uria.set(self.SelectedPatiant[36])
        self.Humo.set(self.SelectedPatiant[37])
        self.Krea.set(self.SelectedPatiant[38])
        self.Na.set(self.SelectedPatiant[39])
        self.K.set(self.SelectedPatiant[40])
        self.Ca.set(self.SelectedPatiant[41])
        self.WBC.set(self.SelectedPatiant[42])
        self.Pro.set(self.SelectedPatiant[43])
        self.Sug.set(self.SelectedPatiant[44])
        self.Beliro.set(self.SelectedPatiant[45])
        self.Fe.set(self.SelectedPatiant[46])
        self.Thyroid.set(self.SelectedPatiant[47])
        self.Urin_Acid.set(self.SelectedPatiant[48])
        self.Evaluation.set(self.SelectedPatiant[49])
        self.Start_Date.set(self.SelectedPatiant[50])
        self.Notification_date.set(self.SelectedPatiant[51])

    def DeletePatiant(self):
        self.Delete_conf = messagebox.askyesno("Rza's Nutrtion Software", "Confirm if you want to delete patiant data")
        if self.Delete_conf > 0:
            self.SearchPatiant = self.PatiantList.curselection()[0]
            self.SelectPatiant = self.PatiantList.get(self.SearchPatiant)
            self.SelectedPatiant = database.ShowPatiantRec(self.SelectPatiant)[0]
            database.DeletePatiantRec(self.SelectedPatiant[1])
            self.ClearData()
            self.ShowData()
    
    def UpdatePatiant(self):
        self.Update_conf = messagebox.askyesno("Rza's Nutrtion Software", "Confirm if you want to Update patiant data")
        if self.Name.get() != 0 and self.Update_conf > 1:
            self.SearchPatiant = self.PatiantList.curselection()[0]
            self.SelectPatiant = self.PatiantList.get(self.SearchPatiant)
            self.SelectedPatiant = database.ShowPatiantRec(self.SelectPatiant)[0]
            database.UpdatePatiantRec(self.SelectedPatiant[0], self.Name.get(), self.Sex.get(), self.Age.get(), self.Status.get(),
                                     self.Address.get(), self.Height.get(), self.Weight_Current.get(), self.Weight_Perfect.get(),
                                     self.Weight_Changed.get(), self.BMI.get(), self.Leather_tuck.get(), self.Arm_Circu.get(),
                                     self.Sick_Prev.get(), self.Sick_Curr.get(), self.Pressure.get(), self.Pulse.get(),
                                     self.Temperature.get(), self.Breath.get(), self.Urin_Exp.get(), self.Cyanosis.get(),
                                     self.Elevate.get(), self.Pallor.get(), self.Dryness.get(), self.Edema.get(), self.Hair.get(),
                                     self.Sleep.get(), self.Constipation.get(), self.Diarrhea.get(), self.Vomiting.get(),
                                     self.Urin_Color.get(), self.Urin_Number.get(), self.Current_sym1.get(),
                                     self.Current_sym2.get(), self.Current_sym3.get(), self.Current_sym4.get(), self.Uria.get(), 
                                     self.Humo.get(), self.Krea.get(), self.Na.get(), self.K.get(), self.Ca.get(), self.WBC.get(),
                                     self.Pro.get(), self.Sug.get(), self.Beliro.get(), self.Fe.get(), self.Thyroid.get(),
                                     self.Urin_Acid.get(), self.Evaluation.get(), self.Start_Date.get(), self.Notification_date.get())
            self.ShowData()
        
    def Schedule(self):
        if path.exists("PatiantBook.db"):
            self.rows = database.ScheduleRec()
            self.day = datetime.now().strftime("%A")
            self.Patiant_List = []
            
            for ID, Name, Day in self.rows:
                if Day == self.day:
                    self.Patiant_List.append(Name)
                    self.Patiant_List.append("and")

            if self.Patiant_List != []:
                self.toaster = ToastNotifier()
                self.toaster.show_toast("Rza's Nutrtion Software", "{} needs a new weekly scedule".format(' '.join(self.Patiant_List)), icon_path = r"C:\Users\majdb\Desktop\Rza\emoji.ico", duration = 10, threaded = True)

    def on_exit(self):
        self.exit_conf = messagebox.askyesno("Rza's Nutrtion Software", "Confirm if you want to exit")
        if self.exit_conf > 0:
            root.quit()
            root.destroy()
            sys.exit()
        
class Menu(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.MainMenu = tk.Menu(self)
        #File_Menu
        self.filemenu = tk.Menu(self.MainMenu, tearoff = 0)
        self.filemenu.add_command(label = "Exit", command = self.on_exit)

    def on_exit(self):
        self.exit_conf = messagebox.askyesno("Rza's Nutrtion Software", "Confirm if you want to exit")
        if self.exit_conf > 0:
            root.quit()
            root.destroy()
            sys.exit()


def main():
    global root, height, width, finish
    root = tk.Tk()
    height = int(root.winfo_screenheight())
    width = int(root.winfo_screenwidth())
    root.geometry(f"{width}x{height}+0+0")
    root.wm_title("Rza's Nutrtion Software")
    root.iconbitmap("ico.ico")
    
    MD = MainDisplay(root)
    MD.pack(side = 'top', fill = 'both', expand = True)
    
    root.mainloop()
    root.quit()

if __name__ == "__main__":
    main()