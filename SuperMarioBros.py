import time

import retro

env = retro.make(game='SuperMarioBros-Nes', record=False)
print(env.action_space)
env.reset()

done = False

while not done:
    env.render()

    #action = env.action_space.sample()
    #print(action)
    action = [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]

    ob, rew, done, info = env.step(action)
    print("ob",ob,"Action ", action, "Reward ", rew, "done ", done, "info", info)
    time.sleep(0.01)

    if done:
        obs = env.reset()

    print(info)

env.close()