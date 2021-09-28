"""Main module."""

import numpy as np
import stable_baselines3 as sb3
from config import settings
from gym_wrapper import UnityEnvToGym

# from stable_baselines3.her import HerReplayBuffer
from stable_baselines3.common.buffers import ReplayBuffer

from unityagents import UnityEnvironment


def train(env, model_class, save_path):
    print({**settings.model_kwargs})
    model = model_class(
        settings.model.policy,
        env,
        **settings.model_kwargs,
    )
    model.learn(**settings.learn_kwargs)
    model.save(save_path)


def viz_agent(env, model_class, save_path):
    # Load the trained agent
    model = model_class.load(save_path, env=env)

    # Enjoy trained agent
    obs = env.reset(train_mode=False)
    for episose in range(3):
        obs = env.reset(train_mode=False)
        for i in range(500):
            action, _states = model.predict(obs, deterministic=True)
            obs, rewards, done, info = env.step(action)
            if done:
                obs = env.reset(train_mode=False)
        print(i)


if __name__ == "__main__":
    # describe_environment()
    model_class = getattr(sb3, settings.model.alg)
    save_path = f"{settings.model.alg}_{settings.model.save_path}"
    print({**settings.unity_env_kwargs})
    unity_env = UnityEnvironment(**settings.unity_env_kwargs)
    env = UnityEnvToGym(unity_env)
    train(env, model_class, save_path)
    # viz_agent(env, model_class, save_path)
