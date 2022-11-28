import time
import random
import retro

class Genetico:
    
    def __init__(self, generaciones):
        self.env = retro.make(game='Airstriker-Genesis', record=False)
        
        self.generaciones = generaciones
        self.cantIndividuos = 20
        self.poblacion = []
        self.jugadas = []
        self.env.reset()
        self.done = False
        self.asignaciones = 0
        self.comparaciones = 0
        self.lineasEjecutadas = 0
        self.tiempoEjecucion = 0

    def generarPoblacionInicial(self):
        self.lineasEjecutadas += 1
        for i in range(self.cantIndividuos):
            self.asignaciones += 7
            self.comparaciones += 1
            self.lineasEjecutadas += 2
            individuo = [random.randint(0,1),random.randint(0,1)]
            self.poblacion.append(individuo)

    def randomPadre(self):
        self.lineasEjecutadas += 2
        self.asignaciones += 3
        padre = self.poblacion[random.randint(0,self.cantIndividuos-1)]
        return padre

    def modificarAction(self, mov):
        self.lineasEjecutadas += 4
        self.asignaciones += 3
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        action[6] = mov[0]
        action[7] = mov[1]

        return action

    def cruceMutacion(self, padre1, padre2):
        self.lineasEjecutadas += 7
        self.asignaciones += 8
        self.comparaciones += 2

        hijoNuevo = []
        genRandom = random.randint(0,1)

        if genRandom == 0:
            self.asignaciones += 1
            self.lineasEjecutadas += 1
            hijoNuevo = [padre1[1], padre2[0]]
        else:
            self.asignaciones += 1
            self.lineasEjecutadas += 1
            hijoNuevo = [padre1[0], padre2[1]]

        porcentajeMutacion = random.randint(0,100)

        if porcentajeMutacion < 5:
            self.asignaciones += 3
            self.lineasEjecutadas += 3
            self.comparaciones += 1
            genAMutar = random.randint(0,1)
            if hijoNuevo[genAMutar] == 0:
                self.asignaciones += 1
                self.lineasEjecutadas += 1
                hijoNuevo[genAMutar] = 1
            else:
                self.asignaciones += 1
                self.lineasEjecutadas += 1
                hijoNuevo[genAMutar] = 0

        self.poblacion.append(hijoNuevo) #agrega el hijo a la poblacion


    def main(self):
        inicio = time.time()
        i = 1
        self.generarPoblacionInicial()
        padre1 = self.randomPadre()
        padre2 = self.randomPadre()

        while i <= self.generaciones:
            time.sleep(0.02)
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
            
            action = self.modificarAction(movimiento)
            
            ob, rew, self.done, info = self.env.step(action)
            if not self.done:
                self.jugadas = self.jugadas + [action]

            i = i + 1

        #print(self.jugadas)

        final = time.time()
        self.tiempoEjecucion = final - inicio
        print("Tiempo:",self.tiempoEjecucion)
        print("Asignaciones:",self.asignaciones)
        print("Comparaciones:",self.comparaciones)
        print("Lineas Ejecutadas:",self.lineasEjecutadas)
        
        
            

p = Genetico(1000)
p.main()

