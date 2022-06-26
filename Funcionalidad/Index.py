from _Clone_Calendar import *
from datetime import datetime
import os
from GuardarCosas import *

def ConvertFileToList(textfile, textfile2):
    
    txtF_1 = FileToList(textfile)
    txtF_2 = FileToList(textfile2)
    
    return txtF_1, txtF_2

def GetCopies(txtF_1, txtF_2):
    UID_tf1 = Leer_IDs(txtF_1)
    UID_tf2 = Leer_IDs(txtF_2)
    UID_tf2 = ( set(UID_tf2) - set(UID_tf1) )
    return UID_tf2
    
def MergeList(FileLines_1, txtF_2, UID_tf2):
    lineas2 = ListaElementos(txtF_2, UID_tf2)
    FileLines_1.extend(lineas2)
    return FileLines_1
    
def List_WithoutDuplicateNames(lineas):
    extract_data = Leer_Datos(lineas)
    
    LeIndexes, LeString = Clones(extract_data)
    Indices_Copia = ListaCopias(LeIndexes, extract_data)
        
    nuevo = Eliminar_Copias(lineas, Indices_Copia)
    return nuevo, extract_data, LeString
   
    
def CalendarioHacer(nuevo):
    calendar1 = CrearEventos(nuevo)
    GuardarArchivo(calendar1)
    
    
    
    
    


#textfile = open(os.path.join('FB_Cal.ics'), encoding="utf8")
#textfile2 = open(os.path.join('G_Cal.ics'), encoding="utf8")

    