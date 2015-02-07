#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
entornos.py
------------


"""
"""
Seis cuartos
"""
__author__ = 'AngelicaMaria'


class Entorno(object):
    """

    """

    def transicion(self, estado, accion):
        """
        @param estado: Tupla con un estado válido para el entorno
        @param accion: Uno de los elementos de acciones_legales( estado)

        @return: el estado a donde transita el entorno cuando el 
                 agente aplica la acción o una tupla de pares ordenados 
                 con el posible estado nuevo y su probabilid
        """
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
        pass

    def sensores(self, estado):
        """
        @param estado: Tupla con un estado válido para el entorno

        @return: Tupla con los valores que se perciben de un entorno

        """
        robot, A, B, C, D, E, F = estado
		return((robot, A , B, C, D, E, F) if robot == 'A' else
			   ('B', A , B, C, D, E, F) if robot == 'B' else
			   ('C', A , B, C, D, E, F)  if robot == 'C' else
			   ('D', A , B, C, D, E, F) if robot == 'D' else
			   ('E', A , B, C, D, E, F) if robot == 'E' else
			   ('F', A , B, C, D, E, F))

        pass

    def desempeno_local(self, estado, accion):
        """
        @param estado: Lista con un estado válido para el entorno
        @param accion: Uno de los elementos de acciones_legales( estado)

        @return: un número flotante con el desempeño de aplicar la accion en el estado

        """
        robot, A, B, C, D, E, F = estado
        return 0 if accion == 'noOp' and A == B == C == D == E == F == 'Limpio' else -1

        pass

    def accion_legal(self, estado, accion):
        """
        @param estado: Tupla con un estado válido para el entorno
        @param accion: Uno de los elementos de acciones_legales( estado)

        @return: Booleano True si la accion es legal en el estado, False en caso contrario

        Por default acepta cualquier acción.
        """

        return True


class Agente(object):
    """
    Clase abstracta para un agente que interactua con un 
    entorno discreto determinista observable.
    """

    def programa(self, percepcion):
        """
        @param percepcion: Lista con los valores que se perciben de un entorno

        @return: accion: Acción seleccionada por el agente, utilizando su programa de agente.

        """
        robot, situacion = percepcion
        if robot == A and A == 'Sucio':
            return (robot, 'Sucio')
        if robot == A and A == 'Limpio':
            return (robot, 'Limpio')
        if robot == B and B == 'Sucio':
            return (robot, 'Sucio')
        if robot == B and B == 'Limpio':
            return (robot, 'Limpio')
        if robot == C and C == 'Sucio':
            return (robot, 'Sucio')
        if robot == C and C == 'Limpio':
            return (robot, 'Limpio')
        if robot == D and D == 'Sucio':
            return (robot, 'Sucio')
        if robot == D and D == 'Limpio':
            return (robot, 'Limpio')
        if robot == E and E == 'Sucio':
            return (robot, 'Sucio')
        if robot == E and E == 'Limpio':
            return (robot, 'Limpio')
        if robot == F and F == 'Sucio':
            return (robot, 'Sucio')
        if robot == F and F == 'Limpio':
            return (robot, 'Limpio')

        pass


def simulador(entorno, agente, estado_inicial, pasos=10, verbose=True):
    """
    Realiza la simulación de un agente actuando en un entorno de forma genérica

    """
    estado = estado_inicial
    performance = 0
    performances = [performance]
    estados = [estado]
    acciones = [None]

    for paso in range(pasos):
        percepcion = entorno.sensores(estado)
        accion = agente.programa(percepcion)
        estado_n = entorno.transicion(estado, accion)
        performance += entorno.desempeno_local(estado, accion)

        performances.append(performance)
        estados.append(estado_n)
        acciones.append(accion)
        estado = estado_n

    if verbose:
        print "Simulacion de entorno tipo" + \
              str(type(entorno)) + \
              "con el agente tipo " + \
              str(type(agente)) + "\n"

        print 'Paso'.center(10) + 'Estado'.center(40) + 'Accion'.center(25) + 'Desempeño \n'.center(15)

        print '_' * (10 + 40 + 25 + 15)
        
        for i in range(pasos):
            print (str(i).center(10) + 
                   str(estados[i]).center(40) +
                   str(acciones[i]).center(25) + 
                   str(performances[i]).rjust(12))
        
        print '_' * (10 + 40 + 25 + 15) + '\n\n'

    return estados, acciones, performances
