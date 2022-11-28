import time
import random
import retro

class Probabilistico:
    def __init__(self):
        self.jugadasCorrectas = []
        self.env = retro.make(game='SuperMarioBros-Nes', record=False)
        self.env.reset()
        self.done = False
        self.posicionX = 0

    def dormir(self):
        time.sleep(0.001)


    def main(self):
        while not self.done:

            if self.posicionX == 0 and len(self.jugadasCorrectas) > 0:
                for i in self.jugadasCorrectas:
                    self.env.render()
                    ob, rew, self.done, info = self.env.step(i)
                    self.dormir()
                    self.posicionX = info['xscrollLo']
                    if self.posicionX == 0:
                        break

            elif self.posicionX > 0 or len(self.jugadasCorrectas) == 0:
                self.dormir()
                self.env.render()

                prob = random.random()
                limite = 0.0
                action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                #0=b 1 2  3   4=Up   5=down  6=left  7=right  8=A  9  10 11

                if prob >= limite:
                    
                    lado = random.randint(0,10)

                    izquierda = 0
                    derecha = 0

                    if lado >= 7:
                        izquierda = 1
                        derecha = 0

                    elif lado < 7:
                        izquierda = 0
                        derecha = 1


                    salto = random.randint(0,10)

                    saltoValor = 0

                    if salto >= 8:
                        saltoValor = 0

                    elif salto < 8:
                        saltoValor = 1

                    action = [0, 0, 0, 0, random.randint(0,1), random.randint(0,1), izquierda, derecha, saltoValor, 0, 0, 0]
                    self.jugadasCorrectas.append(action)
                elif prob < limite:
                    tempIndex = random.randint(0, len(self.jugadasCorrectas))
                    action = self.jugadasCorrectas[tempIndex]
                
                ob, rew, self.done, info = self.env.step(action)
                self.posicionX = info['xscrollLo']
                if self.done:
                    obs = self.env.reset()
                
                print(info)


proba = Probabilistico()
proba.main()