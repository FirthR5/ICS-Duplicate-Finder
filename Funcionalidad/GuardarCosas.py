from icalendar import Calendar
import tempfile, os

def GuardarArchivo(cal):
    #cal.to_ical().replace('\r\n', '\n').strip()
    #pass
    directory = os.getcwd()
    f = open(os.path.join(directory, 'example1.ics'), 'wb')
    f.write(cal.to_ical())
    
   
    f.close()
