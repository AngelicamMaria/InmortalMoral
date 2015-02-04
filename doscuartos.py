#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doscuartos.py.py
------------

Ejemplo de un entorno muy simple y agentes idem

"""

__author__ = 'juliowaissman'

import entornos
from random import choice


class DosCuartos(entornos.Entorno):
    """
	
	***************SIguiene cuestion a modificar
    Clase para un entorno de dos cuartos. Muy sencilla solo regrupa métodos.

    El estado se define como (robot, A, B) donde
    robot puede tener los valores "A", "B"
    A y B pueden tener los valores "limpio", "sucio"

    Las acciones válidas en el entorno son "irA", "irB", "limpiar" y "noOp". Todas las
    acciones son válidas en todos los estados.

    Los sensores es una tupla (robot, limpio?) con la ubicación del robot y el estado de limieza
	
	Para el caso,  de 3 cuartos en cada uno de los 2 pisos.

    """

    def transicion(self, estado, accion):
        if not self.accion_legal(estado, accion):
            raise ValueError("La accion no es legal para este estado")

        robot, A, B, C, D, E, F = estado

        return (('A', A, B, C) if accion == 'irA' else
                ('B', A, B) if accion == 'irB' else
                (robot, A, B) if accion == 'noOp' else
                ('A', 'limpio', B) if accion == 'limpiar' and robot == 'A' else
                ('B', A, 'limpio'))

    def sensores(self, estado):
        robot, A, B = estado
        return robot, A if robot == 'A' else B

    def accion_legal(self, estado, accion):
        return accion in ('irA', 'irB', 'limpiar', 'noOp')

    def desempeno_local(self, estado, accion):
        robot, A, B = estado
        return 0 if accion == 'noOp' and A == B == 'limpio' else -1


class AgenteAleatorio(entornos.Agente):
    """
    Un agente que solo regresa una accion al azar entre las acciones legales

    """
    def __init__(self, acciones):
        self.acciones = acciones

    def programa(self, percepcion):
        return choice(self.acciones)


class AgenteReactivoDoscuartos(entornos.Agente):
    """
    Un agente reactivo simple

    """

    def programa(self, percepcion):
        robot, situacion = percepcion
        return ('limpiar' if situacion == 'sucio' else
                'irDerecha' if robot == 'B' || robot == 'A' else
				'irIzquierda' if robot == 'B' || robot == 'C' else
				'irDerecha' if robot == 'D' || robot == 'E' else
				'irIzquierda' if robot == 'E' || robot == 'F' else
                'Subir' if robot == 'B' || robot == 'C' || robot == 'A' else
				'Bajar'
				)
"""
Si robot, esta en abc, sube, sino, baja. 
Si robot, vaa la derecha es que esta en uno de los dos ultinmos 2 cuartos. No importa el piso. 
Si robot, va a la izquierda es que esta en uno de los primeros 2 cuartos.  No importa el piso.
"""

class AgenteReactivoModeloDosCuartos(entornos.Agente):
    """
    Un agente reactivo basado en modelo

    """
    def __init__(self):
        """
        Inicializa el modelo interno en el peor de los casos

        """
       """ self.modelo = ['A', 'sucio', 'sucio']
        """
		self.modelo = ['A', 'sucio', 'sucio','sucio','Sube'] 
		"""
		Cuarto, Los tres cuartos se muestras si estan juntos, sube o baja
		"""
		self.lugar = {'A': 1, 'B': 2, 'C':3, 'D':4, 'E':5, 'F':6}
		"""
		Los 6 cuartos, del 1 al 6
		"""

    def programa(self, percepcion):
        robot, situacion = percepcion

        # Actualiza el modelo interno
        self.modelo[0] = robot
        self.modelo[self.lugar[robot]] = situacion

        # Decide sobre el modelo interno
		"""
		Se tienen las variables ABCDEF, con los cuartos
		"""
        A,B,C,D,E,F = self.modelo[1], self.modelo[2], self.modelo[3], self.modelo[4], self.modelo[5], self.modelo[6]
        return ('noOp' if A == B == C == D == E == F =='limpio' else
                'limpiar' if situacion == 'sucio' else
                'irDerecha' if robot == 'A' || robot==  'B' else
                'irIzquierda' if robot == 'E' || robot==  'F' else
				'irDerecha' if robot == 'D' || robot==  'E' else
                'irIzquierda' if robot == 'B' || robot==  'C' else
				'Subir' if robot == 'A' || robot == 'B' || robot == 'C' else  
				'Bajar' if robot == 'D' || robot == 'F' || robot == 'E' 
				)
				""""
				Cuartos:
				Piso 2: D,E,F
				Piso 1: A,B,C
				"""


def test():
    """
    Prueba del entorno y los agentes

    """
    print "Prueba del entorno de dos cuartos con un agente aleatorio"
    entornos.simulador(DosCuartos(),
                       AgenteAleatorio(['irA', 'irB', 'limpiar', 'noOp']),
                       ('A', 'sucio', 'sucio'), 100)

    print "Prueba del entorno de dos cuartos con un agente reactivo"
    entornos.simulador(DosCuartos(),
                       AgenteReactivoDoscuartos(),
                       ('A', 'sucio', 'sucio'), 100)

    print "Prueba del entorno de dos cuartos con un agente reactivo"
    entornos.simulador(DosCuartos(),
                       AgenteReactivoModeloDosCuartos(),
                       ('A', 'sucio', 'sucio'), 100)

if __name__ == '__main__':
    test()
