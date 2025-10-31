# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""
#El código simula el funcionamiento de una sala de emergencias 
import time #importa la librería time para manejar tiempos de espera
import datetime #importa la librería datetime para manejar fechas y horas
import modules.paciente as pac # importa el módulo paciente
import random # importa la librería random para generar números aleatorios
from modules.Cola_de_prioridad import ColaDePrioridad # importa la clase ColaDePrioridad 

class salita:
    n = 20  # cantidad de ciclos de simulación
       
    cola_de_espera = ColaDePrioridad()

    # Ciclo que gestiona la simulación
    for i in range(n):
        # Fecha y hora de entrada de un paciente
        ahora = datetime.datetime.now()
        fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
        print('-*-'*15)
        print('\n', fecha_y_hora, '\n')

        # Se crea un paciente un paciente por segundo
        # El nivel de riesgo del paciente es aleatorio
        paciente = pac.Paciente()
        cola_de_espera.encolar(paciente)

        # Atención del paciente en este ciclo: en el 50% de los casos
        if random.random() < 0.5:
        # Se atiende al paciente que se encuentra al frente de la cola
           if not cola_de_espera.esta_vacia():
                paciente_atendido = cola_de_espera.desencolar()
                print('*'*40)
                print('Se atiende el paciente:', paciente_atendido)
                print('*'*40)
        else:
            # se continúa atendiendo paciente de ciclo anterior
            pass
    
        print()
        # Se muestran los pacientes restantes en la cola de espera
        print('Pacientes que faltan atenderse:', cola_de_espera.monticulo.tamanoActual)
        for paciente in cola_de_espera.monticulo.listaMonticulo[1:]:
            print('\t', paciente)
        print()
        print('-*-'*15)
        time.sleep(1)