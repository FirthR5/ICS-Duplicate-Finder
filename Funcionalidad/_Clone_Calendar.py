from icalendar import Calendar, Event,vText
import pytz
import itertools
from difflib import SequenceMatcher

def FileToList(textfile):
    Bool_Evento = False
    tempList = []
    ReturnList = []
    TempTipo=''
    for line in textfile:
        match line:
            case 'END:VEVENT\n':
                Bool_Evento = False 
                ReturnList.append(TempVal)
                continue
            case 'BEGIN:VEVENT\n':
                TempVal={}
                Bool_Evento = True
                TempTipo= ''
                continue
        if Bool_Evento:
            cadena = line.split(':', 1)
            if len(cadena) is 1:
                TempVal[TempTipo] += cadena[0].rstrip("\n")
                continue
                
                        
            Tipo = cadena[0]
            Valor = cadena[1].rstrip("\n")
            TempVal[Tipo] = Valor
            TempTipo = Tipo
            
            
    return ReturnList

def Leer_IDs(register):
    UID_tf1 = []
    for lines in register:
        UID_tf1.append(lines['UID'])
    return UID_tf1

def ListaElementos(register, UID):
    ReturnList = [ lines for lines in register if lines['UID'] in UID ]
    return ReturnList
        
        

def similar(a, b):
    s = SequenceMatcher(None, a, b)
    return s.ratio()


def Capture_Clones(register):
    Lol=[]
    for index, lines in enumerate(register):
        val = lines["SUMMARY"] 
        index2 = index + 1
        tam = len(register)
        if index2>tam: break
        
        for tempIndex in range(index2, (tam-1)):
            if tempIndex>tam-1: break
            
            valorpendejo = register[tempIndex]["SUMMARY"]
            porc = similar(val,  valorpendejo)
            if porc > 0.84:
                tempZz =register.pop(tempIndex)
                
                Lol.append([lines['UID'], val , tempZz['UID'], valorpendejo])
                tam=tam-1
                
        
    return register, Lol



def CrearEventos(registers):
    cal = Calendar()
    for lines in registers:
        event = Event()         
        for key in lines:
            typo = key
            event[typo] = lines[key].rstrip("\n")

        cal.add_component(event)
    return cal







