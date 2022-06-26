import PySimpleGUI as sg
from pathlib import Path

table_content = []

def Estructura():
    sg.theme('SystemDefault')
    
    FilesExp = [
        [
            sg.FileBrowse( file_types=("ICS FILES", "*.ics"), key="-ICS_ID_01-"),
            sg.Text("Choose the First ICS: ")
        ], 
        [
            sg.FileBrowse(file_types=("ICS FILES", "*.ics"), key="-ICS_ID_02-"), 
            sg.Text('Choose the Second ICS' )
        ]
    ]
    columna1 = [
        [sg.Text('Merge Calendars\nSelect the ICS that you want to merge.')],
        FilesExp,
        [sg.Button("Open"), [sg.Button("Guardar Archivo", key='btnSave', visible=False)]]
    ]
    # tabla1 = sg.Table(
    #     headings = ['Nombres:'],
    #     values = table_content,
    #     expand_x = True,
    #     hide_vertical_scroll = True,
    #     key = 'tbl_Nombres'
    # )
    tabla2 = sg.Table(
        headings = ['ID1:','Nombre','ID2:','Nombre_2'],
        values = table_content,
        expand_x = True,
        hide_vertical_scroll = True,
        key = 'tbl_Copias'
    )
    
    layout = [
        [columna1], #[tabla1],
        [tabla2]
    ]
    return layout

