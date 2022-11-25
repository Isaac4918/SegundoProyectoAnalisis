import time
import random
import retro

class Genetico:
    
    def __init__(self):
        self.env = retro.make(game='Airstriker-Genesis', record=True)
        
        self.generaciones = 50
        self.cantIndividuos = 10
        self.poblacion = []
        self.jugadas = []
        self.action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.env.reset()
        self.done = False

    def generarPoblacionInicial(self):
        for i in range(self.cantIndividuos):
            individuo = [random.randint(0,1),random.randint(0,1)]
            self.poblacion.append(individuo)

    def randomPadre(self):
        padre = self.poblacion[random.randint(0,self.cantIndividuos-1)]
        return padre

    def modificarAction(self):
        padre = self.randomPadre()
        self.action[6] = padre[0]
        self.action[7] = padre[1]

    def cruceMutacion(self, padre1, padre2):
        #cruce de padres: single point crossover
        temp1 = padre1[0]
        temp2 = padre2[1]

        padre1[0] = temp2    
        padre2[1] = temp1
        
        print("Padre1 cruce: ", padre1)
        print("Padre2 cruce: ", padre2)
        
        #mutacion de padres a hijos: 
        genRandom = random.randint(0,1)
        print("Gen random para mutar: ", genRandom)
        if genRandom == 0:
            hijoNuevo = [padre1[1], padre2[0]]
        else:
            hijoNuevo = [padre1[0], padre2[1]]

        self.poblacion.append(hijoNuevo) #agrega el hijo a la poblacion nueva


    def main(self):
        i = 1
        self.generarPoblacionInicial()
        print("Poblacion inicial: ", self.poblacion)
 
        #while i <= self.generaciones:
        padre1 = self.randomPadre()
        print("Padre1: ", padre1)
        padre2 = self.randomPadre()
        print("Padre2: ", padre2)

        #self.env.render()
        if not self.done: #evaluacion de los padres
            self.cruceMutacion(padre1, padre2) #cruzamiento los padres, point mutation
            print("Hijo: ", self.poblacion[self.cantIndividuos-1])
            #muta cada elemento de la poblacion excepto los que fueron padres = generacion nueva
            #agarro un random de la poblacion para correrlo en el juego, si la vara no se muere entonces lo agrego a las jugadas
            # ob, rew, self.done, info = self.env.step(self.action)
            #con la nueva generaciones el loop se repite
            print()

        '''if self.done:
            obs = self.env.reset()

        i =+ 1'''
            

p = Genetico()
p.main()
