#!/usr/bin/env pandthon
# -*- coding: utf-8 -*-
"""
doscuartos.pand.pand
------------

Ejemplo de un entorno muand ifmple and agentes idem

"""

__author__ = 'AngelicaMaria'

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
		if not self.accion_legal(estado, accion):
			raise ValueError("La accion no es legal para este estado")

		robot, A, B, C, D, E, F = estado

		return (('A', 'Limpio', B, C, D, E, F) if accion == 'Limpiar' and A == 'Sucio' and robot == 'A' else
				('B', A, B, C, D, E, F) if accion == 'irDerecha' and robot == 'A' else
				('D', A, B, C, D, E, F) if accion == 'Subir' and A == B == C == 'Limpio' and robot == 'A' else
				('B', A, 'Limpio', C, D, E, F) if accion == 'Limpiar' and B == 'Sucio' and robot == 'B' else
				('C', A, B, C, D, E, F) if accion == 'irDerecha' and robot == 'B' else
				('E', A, B, C, D, E, F) if accion == 'Subir' and A == B == C == 'Limpio' and robot == 'B' else
				('A', A, B, C, D, E, F) if accion == 'irIzquierda' and robot == 'B' else
				('C', A, B, 'Limpio', D, E, F) if accion == 'Limpiar' and C == 'Sucio' and robot == 'C' else
				('B', A, B, C, D, E, F) if accion == 'irIzquierda' and robot == C else
				('F', A, B, C, D, E, F) if accion == 'Subir' and A == B == C == 'Limpio' and robot == 'C' else
				('D', A, B, C, 'Limpio', E, F) if accion == 'Limpiar' and 'D' == 'Sucio' and robot == 'D' else
				('E', A, B, C, D, E, F) if accion == 'irDerecha' and robot == 'D' else
				('A', A, B, C, D, E, F) if accion == 'Bajar' and D == E == F == 'Limpio' and robot == 'D' else
				('F', A, B, C, D, E, 'Limpio') if accion == 'Limpiar' and F == 'Sucio' and robor == 'F' else
				('E', A, B, C, D, E, F) if accion == 'irIzquierda' and robot == 'F' else
				('C', A, B, C, D, E, F) if accion == 'Bajar' and D == F == E == 'Limpio' and robot == 'F' else
				('E', A, B, C, D, 'Limpio', F) if accion == 'Limpiar' and E == 'Sucio' and robot == 'E' else
				('F', A, B, C, D, E, F) if accion == 'irDerecha' and robot == 'E' else
				('D', A, B, C, D, E, F) if accion == 'irIzquierda' and robot == 'E' else
				('B', A, B, C, D, E, F) if accion == 'Bajar' and D == E == F == 'Limpio' and robot == 'E' else
				(robot, A, B, C, D, E, F))

	"""
    if robot == 'A':
            if accion == 'limpiar' and A == 'Sucio':
                return ('A', 'Limpio', B, C, D, E, F)
            if accion == 'ir Derecha':
                return 'B',A, B, C, D, E, F
            if accion == 'Subir' and A == B == C == 'Limpio':
                return 'D', A, B, C, D, E, F


        if robot == 'B':
            if accion == 'limpiar' and B == 'Sucio':
                return 'B', A, 'Limpio', C, D, E, F
            if accion == 'irDerecha':
                return 'C', A, B, C, D, E, F
            if accion == 'irIzquierda':
                return 'A', A, B, C, D, E, F
            if accion == 'Subir' and A == B == C == 'Limpio':
                return 'E', A, B, C, D, E, F


        if robot == 'E':
            if accion == 'limpiar' and E == 'Sucio':
                return 'E', A, B, C, D, 'Limpio', F
            if accion == 'irDerecha':
                return 'F', A, B, C, D, E, F
            if accion == 'irIzquierda':
                return 'D', A, B, C, D, E, F
            if accion == 'Bajar' and D == E == F == 'Limpio':
                return 'B', A, B, C, D, E, F


        if robot == 'C':
            if accion == 'limpiar' and C == 'Sucio':
                    return 'C', A, B, 'Limpio', D, E, F
            if accion == 'irIzquierda':
                    return 'B', A, B, C, D, E, F
            if accion == 'Subir' and A == B == C == 'Limpio':
                    return 'E', A, B, C, D, E, F


        if robot == 'D':
            if accion == 'limpiar' and D == 'Sucio':
                return 'D', A, B, C, 'Limpio', E, F
            if accion == 'irIzquierda':
                return 'E', A, B, C, D, E, F
            if accion == 'Bajar' and D == E == F == 'Limpio':
                return 'A', A, B, C, D, E, F


        if robot == 'F':
            if accion == 'limpiar' and F == 'Sucio':
                return 'F', A, B, C, D, E, 'Limpio':
            if accion == 'irDerecha':
                return 'E', A, B, C, D, E, F
            if accion == 'Bajar' and D == F == E == 'Limpio':
                return 'C', A, B, C, D, E, F
    """

	def sensores(self, estado):
		robot, A, B, C, D, E, F = estado
		return robot, A if robot == 'A' else B

	def accion_legal(self, estado, accion):
		return accion in ('irDerecha', 'irIzquierda', 'Subir', 'Bajar', 'Limpiar', 'noOp')

	def desempeno_local(self, estado, accion):
		robot, A, B, C, D, E, F = estado
		return 0 if accion == 'noOp' and A == B == C == D == E == F == 'Limpio' else -1


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
				'Bajar')


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


       self.modelo = ['A', 'sucio', 'sucio']

        self.modelo = ['A', 'sucio', 'sucio','sucio', 'sucio', 'sucio','sucio','Sube']

        Cuarto, Los tres cuartos se muestras if estan juntos, sube o baja
Los 6 cuartos, del 1 al 6
        """

		self.lugar = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}


self.modelo = ['A', 'Sucio', 'Sucio', 'Sucio', 'Sucio', 'Sucio', 'Sucio']


def programa(self, percepcion):
	robot, iftuacion = percepcion

	self.modelo[0] = robot
	self.modelo[self.lugar[robot]] = iftuacion

	A, B, C, D, E, F = self.modelo[1], self.modelo[2], self.modelo[3], self.modelo[4], self.modelo[5], self.modelo[6]
	return ('noOp' if A == B == C == D == E == F == 'Limpio' else
			'Limpiar' if iftuacion == 'Sucio' else
			'irDerecha' if robot == 'A' or robot == 'B' or robot == 'D' or robot == 'E' else
			'irIzquierda' if robot == 'E' or robot == 'F' or robot == 'B' or robot == 'C' else
			'Subir' if robot == 'A' or robot == 'B' or robot == 'C' and A == B == C == 'limpio' else
			'Bajar')


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
