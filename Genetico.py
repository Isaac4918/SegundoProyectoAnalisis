import time
import random
import retro

class Genetico:
    
    def __init__(self):
        self.env = retro.make(game='Airstriker-Genesis', record=True)
        
        self.generaciones = 50
        self.cantIndividuos = 3
        self.poblacion = []
        self.jugadas = []
        self.padres = []
        self.action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.env.reset()
        self.done = False

    def generarIndividuos(self):
        for i in range(self.cantIndividuos):
            individuo = [random.choice([0,1]),random.choice([0,1])]
            self.poblacion.append(individuo)

    def randomPadre(self):
        padre = self.poblacion[random.randint(0,self.cantIndividuos-1)]
        self.padres.append(padre)
        return padre

    def modificarAction(self):
        padre = self.randomPadre()
        self.action[6] = padre[0]
        self.action[7] = padre[1]

    def fitness(self):
        self.env.render()
        ob, rew, self.done, info = self.env.step(self.action)
        #time.sleep(0.5)

        if self.done:
            self.jugadas.append(self.action)
            
        print(self.action)

    def cruceMutacion(self):
        self.fitness()

        while not self.done:
            print()
            

        if self.done:
            obs = self.env.reset()

    def airStriker(self):
        self.fitness()
        self.cruceMutacion()

    def main(self):
        self.generarIndividuos()

        for i in range(self.generaciones):
            self.modificarAction()
            self.fitness()


p = Genetico()
p.main()
