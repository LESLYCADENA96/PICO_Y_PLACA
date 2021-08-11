# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:48:19 2021

@author: LESLY
"""


from PICO_PLACA_class import PICO_PLACA 

""" Main prediction program"""
def main():
    
    """ license format AAA-### """
    """ Date format AA/MM/DD """
    """ Hour format HH:MM """
    
    prog =PICO_PLACA('OBA-7975','2021/6/30','7:50')
    estado = prog.verificar()     
    if estado == "continue":
        estado = prog.validar()
        print("Your vehicle " + estado )  
    else:        
        print(estado)
        
       
    prog =PICO_PLACA('IBM-547','2020/12/24','18:30')
    estado = prog.verificar() 
    if estado == "continue":
        estado = prog.validar()
        print("Your vehicle " + estado )  
    else:        
        print(estado) 
        
    
    prog =PICO_PLACA('GHF-167','2017/5/17','03:00')
    estado = prog.verificar() 
    if estado == "continue":
        estado = prog.validar()
        print("Your vehicle " + estado )  
    else:        
        print(estado)
        
    
    prog =PICO_PLACA('GHF-166','2023/5/17','22:15')
    estado = prog.verificar() 
    if estado == "continue":
        estado = prog.validar()
        print("Your vehicle " + estado )  
    else:        
        print(estado) 
    
    

if __name__ == '__main__':
    main()