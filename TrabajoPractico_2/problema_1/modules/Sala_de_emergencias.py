# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""
import time
import datetime
import modules.paciente as pac
import random
from modules.Cola_de_prioridad import ColaDePrioridad
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
        # La criticidad del paciente es aleatoria
        paciente = pac.Paciente()
        cola_de_espera.encolar(paciente)

        # Atención de paciente en este ciclo: en el 50% de los casos
        if random.random() < 0.5:
        # se atiende paciente que se encuentra al frente de la cola
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