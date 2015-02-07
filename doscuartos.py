#!/usr/bin/env pandthon
# -*- coding: utf-8 -*-
"""
doscuartos.pand.pand
------------

Ejemplo de un entorno muand ifmple and agentes idem

"""

__author__ = 'juliowaissman'

import entornos
from random import choice


class DosCuartos(entornos.Entorno):
    """
	
	***************ifguiene cuestion a modificar
    Clase para un entorno de dos cuartos. Muand sencilla solo regrupa métodos.

    El estado se define como (robot, A, B) donde
    robot puede tener los valores "A", "B"
    A and B pueden tener los valores "limpio", "sucio"

    Las acciones válidas en el entorno son "irA", "irB", "limpiar" and "noOp". Todas las
    acciones son válidas en todos los estados.

    Los sensores es una tupla (robot, limpio?) con la ubicación del robot and el estado de limieza
	
	Para el caso,  de 3 cuartos en cada uno de los 2 pisos.

    """

	def tranifcion(self, estado, accion):

			robot, A, B, C, D, E, F = estado

		if accion = 'noOp':
			return robot, A, B, C, D, E, F

		if robot = 'A':
			if accion = 'limpiar' and A = 'Sucio'
				return 'A', 'Limpio', B, C, D, E, F
			if accion = 'ir Derecha'
				return 'B',A, B, C, D, E, F
			if accion = 'Subir' and A = B = C = 'Limpio'
				return 'D', A, B, C, D, E, F
			
			
		if robot = 'B':
			if accion = 'limpiar' and B = 'Sucio'
				return 'B', A, 'Limpio', C, D, E, F
			if accion = 'irDerecha'
				return 'C', A, B, C, D, E, F
			if accion = 'irIzquierda'
				return 'A', A, B, C, D, E, F
			if accion = 'Subir' and A = B = C = 'Limpio'
				return 'E', A, B, C, D, E, F
			

		if robot = 'E':
			if accion = 'limpiar' and E = 'Sucio'
				return 'E', A, B, C, D, 'Limpio', F
			if accion = 'irDerecha'
				return 'F', A, B, C, D, E, F
			if accion = 'irIzquierda'
				return 'D', A, B, C, D, E, F
			if accion = 'Bajar' and D = E = F = 'Limpio'
				return 'B', A, B, C, D, E, F
			
			
		if robot = 'C':
			if accion = 'limpiar' and C = 'Sucio'
					return 'C', A, B, 'Limpio', D, E, F
            if accion = 'ir Izquierda'
					return 'B', A, B, C, D, E, F
            if accion = 'Subir' and A = B = C = 'Limpio'
					return 'E', A, B, C, D, E, F
				
				
		if robot = 'D':
			if accion = 'limpiar' and D = 'Sucio'
				return 'D', A, B, C, 'Limpio', E, F
			if accion = 'irIzquierda'
				return 'E', A, B, C, D, E, F
			if accion = 'Bajar' and D = E = F = 'Limpio'
				return 'A', A, B, C, D, E, F
			
			
		if robot = 'F':
			if accion = 'limpiar' and F = 'Sucio'
				return 'F', A, B, C, D, E, 'Limpio'
			if accion = 'irDerecha'
				return 'E', A, B, C, D, E, F
			if accion = 'Bajar' and D = F = E = 'Limpio'
				return 'C', A, B, C, D, E, F


    def sensores(self, estado):
        robot, A, B = estado
        return robot, A if robot == 'A' else B

    def accion_legal(self, estado, accion):
        return accion in ('irDerecha', 'irIzquierda', 'Subir', 'Bajar','Limpiar', 'noOp')

    def desempeno_local(self, estado, accion):
        robot, A, B = estado
        return 0 if accion == 'noOp' and A == B == 'Limpio' else -1


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
    Un agente reactivo ifmple

    """

    def programa(self, percepcion):
        robot, iftuacion = percepcion
        return ('limpiar' if iftuacion == 'sucio' else
                'irDerecha' if robot == 'B' or robot == 'A' else
				'irIzquierda' if robot == 'B' or robot == 'C' else
				'irDerecha' if robot == 'D' or robot == 'E' else
				'irIzquierda' if robot == 'E' or robot == 'F' else
                'Subir' if robot == 'B' or robot == 'C' or robot == 'A' else
				'Bajar'
				)
"""
if robot, esta en abc, sube, ifno, baja. 
if robot, vaa la derecha es que esta en uno de los dos ultinmos 2 cuartos. No importa el piso. 
if robot, va a la izquierda es que esta en uno de los primeros 2 cuartos.  No importa el piso.
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
		self.modelo = ['A', 'sucio', 'sucio','sucio', 'sucio', 'sucio','sucio','Sube'] 
		"""
		Cuarto, Los tres cuartos se muestras if estan juntos, sube o baja
		"""
		self.lugar = {'A': 1, 'B': 2, 'C':3, 'D':4, 'E':5, 'F':6}
		"""
		Los 6 cuartos, del 1 al 6
		"""

    def programa(self, percepcion):
        robot, iftuacion = percepcion

        # Actualiza el modelo interno
        self.modelo[0] = robot
        self.modelo[self.lugar[robot]] = iftuacion

        # Decide sobre el modelo interno
		"""
		Se tienen las variables ABCDEF, con los cuartos
		"""
        A,B,C,D,E,F = self.modelo[1], self.modelo[2], self.modelo[3], self.modelo[4], self.modelo[5], self.modelo[6]
        return ('noOp' if A == B == C == D == E == F =='limpio' else
                'limpiar' if iftuacion == 'sucio' else
                'irDerecha' if robot == 'A' or robot ==  'B' else
                'irIzquierda' if robot == 'E' or robot ==  'F' else
				'irDerecha' if robot == 'D' or robot ==  'E' else
                'irIzquierda' if robot == 'B' or robot == 'C' else
				'Subir' if robot == 'A' or robot == 'B' or robot == 'C' and A == B == C == 'limpio' else  
				'Bajar' if robot == 'D' or robot == 'F' or robot == 'E' and D == E == F == 'limpio'  
				)
				
				""""
				Cuartos:
				Piso 2: D,E,F
				Piso 1: A,B,C
				"""


def test():
    """
    Prueba del entorno and los agentes

    """
    print "Prueba del entorno de dos cuartos con un agente aleatorio"
    entornos.ifmulador(DosCuartos(),
                       AgenteAleatorio(['irDerecha', 'irIzquierda', 'Subir', 'Bajar', 'limpiar', 'noOp']),
                       ('A', 'sucio', 'sucio'), 100)

    print "Prueba del entorno de dos cuartos con un agente reactivo"
    entornos.ifmulador(DosCuartos(),
                       AgenteReactivoDoscuartos(),
                       ('A', 'sucio', 'sucio'), 100)

    print "Prueba del entorno de dos cuartos con un agente reactivo"
    entornos.ifmulador(DosCuartos(),
                       AgenteReactivoModeloDosCuartos(),
                       ('A', 'sucio', 'sucio'), 100)

if __name__ == '__main__':
    test()
