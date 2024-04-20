

def single_bot_game(env,bot,episodes = 10):
    hit_cnt = 0 
    for i in range (episodes):
        done = False
        (state,info) = env.reset()
        score = 0 
        while(done == False):
            (action,value) = bot.predict(state)
            (state,reward,done,truncated,info) = env.step(action)
            score += reward
            if(info['hit']==True):
                hit_cnt+=1
        print(f"Episode {i+1} score: {score}")
    print("Hit percentage : ", hit_cnt/(episodes * env.action_cnt))

def get_updated_state(state):
    updated_state = [800-x for x in state[:-1]]
    updated_state.reverse()
    updated_state.append(state[-1])
    return updated_state

def compete_bots(env, bot_1,bot_2, episodes=10):
    hit_cnt_1 = 0
    hit_cnt_2 = 0
    for i in range(episodes):
        done = False
        (state,info) = env.reset()
        score_1 = 0
        score_2 = 0 
        while(done == False):
            (action,value) = bot_1.predict(state)
            (state,reward,done,truncated,info) = env.step(action,0)
            score_1 += reward
            if(info['hit']==True):
                hit_cnt_1+=1
            updated_state = get_updated_state(state)
            (action,value) = bot_2.predict(updated_state)
            (state,reward,done,truncated,info) = env.step(action,1)
            score_2 += reward
            if(info['hit']==True):
                hit_cnt_2+=1
        print(f"Episode {i+1} score -> bot 1 score : {score_1} | bot 2 score : {score_2} ")
    print("Tank 1 hit percentage : ", hit_cnt_1/(episodes*env.action_cnt))
    print("Tank 2 hit Percentage : ", hit_cnt_2/(episodes*env.action_cnt))

