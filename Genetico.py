import time
import random
import retro

class Genetico:
    
    def __init__(self):
        self.env = retro.make(game='Airstriker-Genesis', record=False)
        
        self.generaciones = 2000
        self.cantIndividuos = 20
        self.poblacion = []
        self.jugadas = []
        

        self.env.reset()
        self.done = False

    def generarPoblacionInicial(self):
        for i in range(self.cantIndividuos):
            individuo = [random.randint(0,1),random.randint(0,1)]
            self.poblacion.append(individuo)

    def randomPadre(self):
        padre = self.poblacion[random.randint(0,self.cantIndividuos-1)]
        return padre

    def modificarAction(self, mov):
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        action[6] = mov[0]
        action[7] = mov[1]

        return action

    def cruceMutacion(self, padre1, padre2):
        hijoNuevo = []
        genRandom = random.randint(0,1)

        if genRandom == 0:
            hijoNuevo = [padre1[1], padre2[0]]
        else:
            hijoNuevo = [padre1[0], padre2[1]]

        porcentajeMutacion = random.randint(0,100)

        if porcentajeMutacion < 5:
            genAMutar = random.randint(0,1)
            if hijoNuevo[genAMutar] == 0:
                hijoNuevo[genAMutar] = 1
            else:
                hijoNuevo[genAMutar] = 0

        self.poblacion.append(hijoNuevo) #agrega el hijo a la poblacion


    def main(self):
        i = 1
        self.generarPoblacionInicial()
 
        while i <= self.generaciones:
            padre1 = self.randomPadre()
            padre2 = self.randomPadre()
            time.sleep(0.01)
            print("///////////Generacion ", i)
            self.env.render()

            if self.done:
                obs = self.env.reset()
                self.env.close()
                return

            if i >= 2:
                jugadaAnterior = self.jugadas[len(self.jugadas)-1]
                
                padre1 = [jugadaAnterior[6], jugadaAnterior[7]]
                padre2 = self.randomPadre()

            
            self.cruceMutacion(padre1, padre2)
            movimiento = self.poblacion[random.randint(0,len(self.poblacion)-1)]
            
            action = self.modificarAction(movimiento) #agarro un random de la poblacion para correrlo en el juego, si la vara no se muere entonces lo agrego a las jugadas
            
            ob, rew, self.done, info = self.env.step(action)
            if not self.done:
                self.jugadas = self.jugadas + [action]

            i = i + 1

        print(self.jugadas)
        
        
            

p = Genetico()
p.main()

