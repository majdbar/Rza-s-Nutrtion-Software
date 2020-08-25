# -*- coding: utf-8 -*-
"""
Created by Majd Barchini on 08/20/2020

cmd : python setup.py build
"""

import sys
import os
from cx_Freeze import setup, Executable

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base = "Console"
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("main.py", base = base, icon = "ico.ico")]

build_exe_options = {"packages": ["tkinter", "datetime", "sys", "PIL", "cv2", "os", 
                                  "PIL._imagingtk", "PIL.ImageTk", "win10toast", "sqlite3"],
                      "include_files": [(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                                          os.path.join('lib', 'tk86t.dll')),
                                          (os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                                          os.path.join('lib', 'tcl86t.dll')),
                                          "ico.ico"]}#add icon

setup(name="Rza's Nutrtion Software",
      version="1.0",
      author = 'Majd Barchini',
      description="Rza's Nutrtion Software",
      options = {"build_exe": build_exe_options},
      executables = executables)