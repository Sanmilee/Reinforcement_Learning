# CartPole has two basic actions[0=left, 1=right]

import gym

# choose one of OpenAI Gym built in Env called CartPole
env = gym.make('CartPole-v0')

# reset the created Env to default
env.reset()

# run action for a number of time = 1000 times
for steps in range(1000):

    # render function is used to visualize/display
    env.render()

    # create random actions using --- action_space funct
    env.step(env.action_space.sample())
