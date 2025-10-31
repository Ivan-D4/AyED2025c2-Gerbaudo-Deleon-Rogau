# -*- coding: utf-8 -*-

from random import randint, choices
import time
import datetime

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self): #Inicializa un paciente con datos aleatorios
        n = len(nombres) #calcula cantidad de nombres disponibles
        self.__nombre = nombres[randint(0, n-1)] #elige un nombre aleatorio
        self.__apellido = apellidos[randint(0, n-1)] #elige un apellido aleatorio
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0] #elige un nivel de riesgo aleatorio
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1] #asigna la descripción correspondiente al riesgo 
        self.__hora = datetime.datetime.now() #registra la hora de "llegada" del paciente
        self.__llegada = self.__hora # guarda la hora con el momento de llegada para comparaciones

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def get_hora(self):
        return self.__hora
    
    def __str__(self): #Construye una cadena con paciente, apellido, riesgo y descripción
        cad = self.__nombre + ' ' 
        cad += self.__apellido + '\t -> ' 
        cad += str(self.__riesgo) + '-' + self.__descripcion 
        return cad
        
    def __lt__(self, otro): # Compara hora de llegada si hay igual nivel de riesgo u ordena por prioridad 
        # el paciente que llegó antes tiene mayor prioridad
        if self.__riesgo == otro.__riesgo: 
            return self.__llegada < otro.__llegada 
        else: 
            return self.__riesgo < otro.__riesgo

    def __gt__(self, otro): # Compara hora de llegada si hay igual nivel de riesgo u ordena por prioridad 
        # el paciente que llegó despues tiene menor prioridad
        if self.__riesgo == otro.__riesgo:
            return self.__llegada > otro.__llegada
        else:
            return self.__riesgo > otro.__riesgo

    def __eq__(self, otro): # Compara si dos pacientes son iguales en nivel de riesgo y hora de llegada
        return self.__riesgo == otro.__riesgo and self.__llegada == otro.__llegada
    
        