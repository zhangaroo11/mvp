""" Log standard MVP sensors
"""

from SI7021 import *
from Recorder import record_env


def log_sensors(test = True):

    si=SI7021()

    try:
        temp = si.get_tempC()

        status = 'Success'
        if test:
            status = 'Test'
        record_env('Environment_Observation', 'Air', 'Top', 'Temperature', "{:10.1f}".format(temp), 'SI7021', status)                
    except Exception as e:
        status = 'Failure'
        if test:
            status = 'Test'
        record_env('Environment_Observation', 'Air', 'Top', 'Temperature', '', 'SI7021', status, comment=str(e))                            

    try:
        humid = si.getHumidity()

        status = 'Success'
        if test:
            status = 'Test'
        record_env('Environment_Observation', 'Air', 'Top', 'Humidity', "{:10.1f}".format(humid), 'SI7021', status)                
        
    except Exception as e:
        status = 'Failure'
        if test:
            status = 'Test'
        record_env('Environment_Observation', 'Air', 'Top', 'Humidity', '', 'SI7021', status, comment=str(e))                                        
            

def test():
    log_sensors(True)

if __name__=="__main__":
    log_sensors()    