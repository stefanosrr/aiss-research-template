"""Settings shared by every Python script. Stata counterpart: code/00_setup.do

    from lib.settings import SEED
    rng = np.random.default_rng(SEED)
"""
SEED = 20261020  # same number as `set seed` in 00_setup.do: set once per project, then never change it
