"""
Proyecto 2 Análisis de algoritmos
Isaac Araya Solano 2018151703
Alexia Cerdas Aguilar 2019026961
"""

import time
import random
import retro

class Genetico:
    def __init__(self, generaciones):
        self.env = retro.make(game='Airstriker-Genesis', record=False)
        
        self.generaciones = generaciones
        self.cantIndividuos = 500
        self.poblacion = []
        self.poblacionFitness = []
        self.env.reset()
        self.asignaciones = 7 # Conteo
        self.comparaciones = 0 # Conteo
        self.lineasEjecutadas = 0 # Conteo
        self.tiempoEjecucion = 0 # Conteo


    def generarPoblacionInicial(self): #6m
        self.lineasEjecutadas += 1 # Conteo
        for i in range(self.cantIndividuos):
            self.asignaciones += 7 # Conteo
            self.comparaciones += 1 # Conteo
            self.lineasEjecutadas += 2 # Conteo
            individuo = [random.randint(0,1),random.randint(0,1)]
            self.poblacion.append(individuo)


    def randomPadre(self): #5
        self.lineasEjecutadas += 2 # Conteo
        self.asignaciones += 4 # Conteo
        padre = self.poblacionFitness[random.randint(0,len(self.poblacionFitness)-1)]
        return padre


    def crearAccion(self, mov): #4
        self.lineasEjecutadas += 4 # Conteo
        self.asignaciones += 3 # Conteo
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        action[6] = mov[0]
        action[7] = mov[1]

        return action


    def cruceMutacion(self, padre1, padre2): #18
        self.lineasEjecutadas += 7 # Conteo
        self.asignaciones += 8 # Conteo
        self.comparaciones += 2 # Conteo

        hijoNuevo = []
        genRandom = random.randint(0,3)

        if genRandom == 0:
            self.asignaciones += 1 # Conteo
            self.lineasEjecutadas += 1 # Conteo
            hijoNuevo = [padre1[0], padre1[1]]
        
        elif genRandom == 1:
            self.asignaciones += 1 # Conteo
            self.lineasEjecutadas += 1 # Conteo
            hijoNuevo = [padre2[0], padre2[1]]

        elif genRandom == 2:
            self.asignaciones += 1 # Conteo
            self.lineasEjecutadas += 1 # Conteo
            hijoNuevo = [padre1[0], padre2[1]]

        elif genRandom == 3:
            self.asignaciones += 1 # Conteo
            self.lineasEjecutadas += 1 # Conteo
            hijoNuevo = [padre2[0], padre1[1]]

        porcentajeMutacion = random.randint(0,100)

        if porcentajeMutacion < 5:
            self.asignaciones += 3 # Conteo
            self.lineasEjecutadas += 3 # Conteo
            self.comparaciones += 1 # Conteo

            genAMutar = random.randint(0,1)

            if hijoNuevo[genAMutar] == 0:
                self.asignaciones += 1 # Conteo
                self.lineasEjecutadas += 1 # Conteo
                hijoNuevo[genAMutar] = 1
            else:
                self.asignaciones += 1 # Conteo
                self.lineasEjecutadas += 1 # Conteo
                hijoNuevo[genAMutar] = 0

        self.poblacion.append(hijoNuevo) #agrega el hijo a la poblacion


    def crearNuevaGeneracion(self): #28m+1
        self.asignaciones += 2 # Conteo
        self.lineasEjecutadas += 2 # Conteo
        self.comparaciones += 1 # Conteo

        self.poblacion = []
        for i in range(0,self.cantIndividuos):

            self.asignaciones += 4 # Conteo
            self.lineasEjecutadas += 3 # Conteo
            self.comparaciones += 1 # Conteo

            padre1 = self.randomPadre()
            padre2 = self.randomPadre()
            self.cruceMutacion(padre1, padre2)


    def main(self):
        inicio = time.time()
        for i in range(0, self.generaciones):
            if i == 0: #1
                self.generarPoblacionInicial() #6m
            else:
                self.crearNuevaGeneracion() #28m+1
                self.poblacionFitness = [] #1

            for indiv in range(0, len(self.poblacion)): #17m
                #time.sleep(0.02)
                #print("-->Generacion:", i+1, "| Individuo:", indiv+1)
                self.env.render() #1

                action = self.crearAccion(self.poblacion[indiv]) #7

                ob, rew, done, info = self.env.step(action) #6

                if info['gameover'] == 9: #1
                    self.poblacionFitness.append(self.poblacion[indiv]) #2
                
            self.env.reset() #1

        #51mn + 4n

        final = time.time()
        self.tiempoEjecucion = final - inicio
        print("Asignaciones:",self.asignaciones)
        print("Comparaciones:",self.comparaciones)
        print("Lineas Ejecutadas:",self.lineasEjecutadas) 
        print("Tiempo:",self.tiempoEjecucion)
        
p = Genetico(90)
p.main()