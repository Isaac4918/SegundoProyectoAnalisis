import time
import random
import retro

env = retro.make(game='Airstriker-Genesis', record=True)
generaciones = 100
cantIndividuos = 3
poblacion = []
jugadas = [] #una matriz historia de lista de jugadas: guardarlo en un txt al final
env.reset()

#random de la poblacion de dos padres
done = False

while not done:
    env.render()
    #hacer la funcion fitness: preguntar si el juego finalizó con variable done o info
    #cruce la siguiente población, movimiento anterior + escoger un mov de la poblacion anterior al azar
    #generar la población mayor a 2 (mutar) y se escoge uno
    #escoger un movimiento de forma aleatoria para correrlo en el juego

    # action = env.action_space.sample()
    action = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    # se usa 0 = B, 4 = UP, 5 = DOWN, 6 = LEFT, 7 = RIGHT, 8 = A

    ob, rew, done, info = env.step(action)
    print("ob", ob,"Action ", action, "Reward ", rew, "done ", done, "info", info)
    #time.sleep(0.5)

if done:
    obs = env.reset()

env.close()