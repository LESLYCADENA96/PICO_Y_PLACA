# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:48:19 2021

@author: LESLY
"""


from PICO_PLACA_class import PICO_PLACA 

""" Main program of "Pico y Placa" predictor"""
def main():
    
    print("Predictor")
    
    placa = input("Enter the license of your vehicle in the following format AAA-####:  ")
    
    fecha = input("Enter the date in the following format AA/MM/DD:  ")    
    
    hora = input("Enter the time in the following format 00:00:  ")    

    
    prog =PICO_PLACA(placa,fecha,hora)
    estado = prog.verificar() 
    
    if estado == "continue":
        estado = prog.validar()
        print("Your vehicle " + estado )  
    else:        
        print(estado)

if __name__ == '__main__':
    main()