from Layout_ import *
import PySimpleGUI as sg

import sys, os
sys.path.append('../ICS-Duplicate-Finder/Funcionalidad')
from Index import *

window = sg.Window('Merge Calendar', Estructura())

while True:
    event, values = window.read() 
    if event == sg.WIN_CLOSED:
        break
    if event == 'Open':
        LeFile1 = values['-ICS_ID_01-']
        LeFile2 = values['-ICS_ID_02-']
        if Path(LeFile1).is_file() and Path(LeFile2).is_file():
            LeFile1 = open(os.path.join(LeFile1), encoding="utf8")
            LeFile2 = open(os.path.join(LeFile2), encoding="utf8")
            
            txtF_1, txtF_2 = ConvertFileToList(LeFile1, LeFile2)
            UID_tf2 = GetCopies(txtF_1, txtF_2)
            lista = MergeList(txtF_1,txtF_2,UID_tf2)
            
            register, Lol = List_WithoutDuplicateNames(lista)
            
            window['tbl_Copias'].update(Lol)
            window['btnSave'].update(visible=True)
    if event == 'btnSave':
        CalendarioHacer(register)
        
window.close()

