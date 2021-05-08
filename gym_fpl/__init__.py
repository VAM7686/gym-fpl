from gym.envs.registration import register

register(
        id = 'fpl-v0',
        entry_point = 'gym_fpl.envs:fplEnv',
)


register(
        id = 'fpl-chips-v0',
        entry_point = 'gym_fpl.envs:fplChipsEnv',
)
