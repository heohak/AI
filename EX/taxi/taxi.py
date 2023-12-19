import gymnasium as gym
import numpy as np
import random
import matplotlib.pyplot as plt

alpha = 0.1
gamma = 0.6
epsilon = 0.1

env = gym.make("Taxi-v3")

state_space = 500  # 25 taxi positions x 5 passenger locations x 4 destinations
action_space = 6   # 4 directions, 1 pickup, 1 dropoff

q_table = np.zeros([state_space, action_space])

episode_scores = []

# Action selection function
def choose_action(state, epsilon):
    if not isinstance(state, int):
        raise TypeError(f"State is not an integer: {state} (type: {type(state)})")
    if random.uniform(0, 1) < epsilon:
        return env.action_space.sample()
    else:
        return np.argmax(q_table[state])

# Training the agent
for i in range(1, 10100):
    state = env.reset()
    if not isinstance(state, int):
        state = state[0]

    epochs, penalties, reward = 0, 0, 0
    done = False
    episode_score = 0

    while not done:
        action = choose_action(state, epsilon)
        next_state, reward, terminated, truncated, info = env.step(action)
        if not isinstance(next_state, int):
            next_state = next_state[0]

        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])

        q_table[state, action] = old_value + alpha * (float(reward) + gamma * next_max - old_value)

        if reward == -10:
            penalties += 1

        state = next_state
        epochs += 1
        episode_score += reward

        if terminated or truncated:
            break

    episode_scores.append(episode_score)

    if epsilon > 0.01:
        epsilon *= 0.99995

# Plotting episode scores
plt.figure(figsize=(12, 6))
plt.plot(episode_scores, label='Episode Scores')
plt.xlabel('Episodes')
plt.ylabel('Score')
plt.title('Episode Scores During Training')
plt.legend()
plt.savefig('episode_scores.png')  # Save the figure
plt.show()

# Test the trained agent
print("Testing the trained agent...")
for episode in range(5):
    state = env.reset()
    if not isinstance(state, int):
        state = state[0]

    epochs, penalties, reward = 0, 0, 0
    done = False
    print(f"Episode: {episode + 1}")

    while not done:
        action = np.argmax(q_table[state])
        next_state, reward, terminated, truncated, info = env.step(action)
        if not isinstance(next_state, int):
            next_state = next_state[0]

        if reward == -10:
            penalties += 1

        state = next_state
        epochs += 1

        if terminated or truncated:
            break

    print(f"Timesteps: {epochs}, Penalties: {penalties}")
