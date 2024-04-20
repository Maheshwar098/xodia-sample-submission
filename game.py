from stable_baselines3 import A2C
from train import CustomEnv
from utils import *


env = CustomEnv()
bot_1_path = "./trained_bots/bot.zip"
bot_2_path = "./trained_bots/bot.zip"

bot_1 = A2C.load(bot_1_path, env=env)
bot_2 = A2C.load(bot_2_path, env=env)

episodes = 5
single_bot_game(env,bot_1,episodes)
compete_bots(env,bot_1,bot_2,episodes)