import gym
import numpy as np
from gym import spaces


class UnityEnvToGym(gym.Env):
    """Custom Environment that follows gym interface"""

    metadata = {"render.modes": ["human"]}

    def __init__(self, unity_env):
        super(UnityEnvToGym, self).__init__()
        self.unity_env = unity_env
        self.brain_name = self.unity_env.brain_names[0]
        brain = self.unity_env.brains[self.brain_name]
        env_info = self.unity_env.reset(train_mode=True)[self.brain_name]
        self.action_space = spaces.Discrete(brain.vector_action_space_size)
        state = env_info.vector_observations[0]
        self.observation_space = spaces.Box(
            low=0, high=1, shape=(len(state),), dtype=np.float16
        )

    def step(self, action):
        # Execute one time step within the environment
        env_info = self.unity_env.step(action)[self.brain_name]
        next_state = env_info.vector_observations[0]  # get the next state
        reward = env_info.rewards[0]  # get the reward
        done = env_info.local_done[0]
        return next_state, reward, done, {}

    def reset(self, **kwargs):
        train_mode = kwargs.pop("train_mode", True)
        env_info = self.unity_env.reset(train_mode=train_mode)[self.brain_name]
        return env_info.vector_observations[0]
