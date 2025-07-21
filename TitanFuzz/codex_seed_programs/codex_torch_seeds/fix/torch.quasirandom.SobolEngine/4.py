'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quasirandom.SobolEngine\ntorch.quasirandom.SobolEngine(dimension, scramble=False, seed=None)\n'
import torch
import numpy as np
dim = 3
num_samples = 100
sobol_engine = torch.quasirandom.SobolEngine(dim)
samples = sobol_engine.draw(num_samples)
print('samples:', samples)
sobol_engine = torch.quasirandom.SobolEngine(dim, scramble=True)
scrambled_samples = sobol_engine.draw(num_samples)
print('scrambled_samples:', scrambled_samples)
sobol_engine = torch.quasirandom.SobolEngine(dim, seed=1)
seeded_samples = sobol_engine.draw(num_samples)
print('seeded_samples:', seeded_samples)