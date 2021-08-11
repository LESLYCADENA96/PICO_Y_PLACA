# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:32:23 2021

@author: LESLY
"""


import datetime

""""PREDICTOR PICO Y PLACA"""

class PICO_PLACA():
    
    """Declaration of variables"""
    
    def __init__(self, placa, fecha, hora):
        self.hora = hora                
        self.placa = placa              
        self.fecha = fecha              


    """Verification function"""
    def verificar(self):
            
        fecha2 = self.fecha.split("/")              
        hora2 = self.hora.split(":")                      
        
        if int(fecha2[1]) < 1 or int(fecha2[1]) > 12: 
            
            estado = "Error introduce a real date"             
            
        elif int(fecha2[2]) < 1 or int(fecha2[2]) > 31: 
            
            estado = "Error introduce a real date"            
            
        elif int(hora2[0]) < 0 or int(hora2[0]) > 24: 
            
            estado = "Error introduce a real hour"             
            
        elif int(hora2[1]) < 0 or int(hora2[1]) > 60: 
            
            estado = "Error introduce a real hour"
            
        else:
            estado = "continue"
        
        return estado
             
    
    """Validation function"""   
    def validar(self):
        
        id_last = self.placa[len(self.placa)-1]     
        fecha2 = self.fecha.split("/")              
        hora2 = self.hora.split(":")     
        
        dia = datetime.date(int(fecha2[0]),int(fecha2[1]),int(fecha2[2])).isoweekday()
        
        
        """ Check if the vehicle can be on road or not """
        if dia == 1 and ( id_last == "1" or id_last == "2" ):
            
            estado = "can NOT be on the road"
        
        elif dia == 2 and (id_last == "3" or id_last == "4"):
            
            estado = "can NOT be on the road"
        
        elif dia == 3 and (id_last == "5" or id_last == "6") :
            
            estado = "can NOT be on the road"
        
        elif dia == 4 and (id_last == "7" or id_last == "8") :
        
            estado = "can NOT be on the road"
        
        elif dia == 5 and (id_last == "9" or id_last == "0") :
            
            estado = "can NOT be on the road"
        
        else:
            
            estado = "can be on the road"
       
        
        """Range of hours that vehicle can move"""
        minutos = (int(hora2[0])*60)+int(hora2[1])
        
        if estado == "can NOT be on the road":       
            
            if minutos >= 420 and minutos < 569:
                
                estado = "can NOT be on the road"
                
            elif minutos >= 960 and minutos < 1169:
                
                estado = "can NOT be on the road"
            
            else:
                
                estado = "can be on the road"            
        
        return estado 
    
    
 

 
     
