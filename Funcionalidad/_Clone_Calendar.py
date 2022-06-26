from icalendar import Calendar, Event,vText
import pytz
import itertools
from difflib import SequenceMatcher

def FileToList(textfile):
    Bool_Evento = False
    tempList = []
    ReturnList = []
    
    for line in textfile:
        match line:
            case 'END:VEVENT\n':
                Bool_Evento = False 
                ReturnList.append(tempList)
                tempList =[]
                continue
            case 'BEGIN:VEVENT\n':
                Bool_Evento = True
                continue
        if Bool_Evento:
            tempList.append(line)
    return ReturnList

def Leer_IDs(register):
    UID_tf1 = []
    for lines in register:
        for line in lines:
            if line.rpartition(':')[0] == "UID":
                UID_tf1.append(line.rpartition(':')[2])
    return UID_tf1

def ListaElementos(register, UID):
    tempList = []
    ReturnList = []
    for lines in register:
        iteration = 0
        Bin_L = True
        for line in lines:
            iteration +=1
            LineType = line.rpartition(':')[0]
            
            if LineType == "UID":
                valz = line.rpartition(':')[2]
                
                if valz not in UID: 
                    Bin_L = False
                    tempList=[]
                else:
                    UID.pop()
                    
            if Bin_L:
                tempList.append(line)
                if iteration>= len(lines):
                    ReturnList.append(tempList) 
                
    return ReturnList

def Leer_Datos(register):
    extract_data = {
        "UID": [],
        "SUMMARY": [],
        "DTSTAMP": []        
    }
    for lines in register:
        for line in lines:
            valor = line.rpartition(':')[0]
            match valor:
                case "SUMMARY":
                    extract_data["SUMMARY"].append(line.rpartition(':')[2])
                case "DTSTAMP":
                    extract_data["DTSTAMP"].append(line.rpartition(':')[2])
                case "UID":
                    extract_data["UID"].append(line.rpartition(':')[2])
    return extract_data   

def similar(a, b):
    s = SequenceMatcher(None, a, b)
    return s.ratio()

def Clones(extract_data1):
    LeIndexes = []
    LeString = []
    #ToDo: luego implementar si es el mismo dia
    for index, curret_value in enumerate(extract_data1["SUMMARY"]):
        index2 = index
        for index2 in range(index2 + 1, len(extract_data1["SUMMARY"])):
            compare_value = extract_data1["SUMMARY"][index2]
            porcentaje = similar(curret_value, compare_value )
            if  porcentaje > 0.84:
                curret_value = curret_value.rstrip("\n")
                compare_value =compare_value.rstrip("\n")
                temp = [index, curret_value, index2,compare_value, (porcentaje*100)]
                LeString.append(temp)
                LeIndexes.append(index2)
                
    return LeIndexes, LeString
    
def ListaCopias(LeIndexes, extract_data1):
    Ls = []
    for i, n in enumerate(extract_data1["UID"]):
        if i in LeIndexes:
          Ls.append(n)
    return Ls

def Eliminar_Copias(register, Indices_Copia):
    for index, lines in enumerate(register):
        for line in lines:
            lineType = line.rpartition(':')[0]
            if lineType == "UID":
                lineID = line.rpartition(':')[2]
                if lineID in reversed(Indices_Copia):
                    register.pop((index - 1))
                    
    return register


def CrearEventos(registers):
    cal = Calendar()
    for lines in registers:
        Bool_Evento = True
        event = Event() 
        for line in lines:
            lineType =  line.split(':')[0]
            lineType.lower()
            try:
                valor = line.split(':')[1].split('\n')[0]
                if lineType == "DESCRIPTION":
                    valor = ':'.join([str(item) for item in line.split(':')[1:]]).rstrip("\n")
                event[lineType] =  valor            
            except:
                event['DESCRIPTION'] += line[1:].rstrip("\n")
        cal.add_component(event)
        event = None
    return cal


