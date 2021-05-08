import gym
from gym import error, spaces, utils
from gym.utils import seeding

class fplEnv(gym.Env):
  """Base environment for the game of fantasy premier league.
    At any given timestep, the env expects a legal move for the current player, otherwise an Error is raised.

    The agent is awarded a reward of the points it has scored in the gameweek. The agent receives a reward of -4 for each transfer over the free transfer limit.

    Observations and actions are represented as `Game` and `Move` objects, 
    respectively. The actual encoding as numpy arrays is left to wrapper classes
    for flexibility and separation of concerns (see the `wrappers` module for 
    examples). As a consequence, the `observation_space` and `action_space`
    members are set to `None`.

    Observation:
        Type: Game
        Note: Modifying the returned `Game` instance does not modify the internal state of this env.
    Actions:
        Type: Move
        Note: Simply a transfer
    Reward:
        Points for the previous gameweek
    Starting State:
        Unlimited transfers and 100 M to pick players. Or a given team.
    Episode Termination:
        Last gameweek.
    """

  metadata = {'render.modes': ['human']}

  def __init__(self):
    ...
  def step(self, action):
    ...
  def reset(self):
    ...
  def render(self, mode='human'):
    ...
  def close(self):
    ...
  def legal_moves(self):
    