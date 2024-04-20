from Xodia24.env import PocketTank
from stable_baselines3 import A2C

class CustomEnv(PocketTank):
    def _get_reward(self,diff,bullet_type):
        reward = None
        if(diff==0):
            return 100
        else : 
            return ((1/diff**2)*((18-diff)**3))
        return reward

env = CustomEnv()

bot = A2C(policy='MlpPolicy', env=env, verbose = 1)

if __name__ == '__main__':
    bot.learn(total_timesteps=300000)

    bot.save("./trained_bots/bot")
