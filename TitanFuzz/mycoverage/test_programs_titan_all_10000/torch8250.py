import torch
from torch import nn
from torch.autograd import Variable
dim = 3
num_samples = 100
sobol_engine = torch.quasirandom.SobolEngine(dim)
samples = sobol_engine.draw(num_samples)
sobol_engine = torch.quasirandom.SobolEngine(dim, scramble=True)
scrambled_samples = sobol_engine.draw(num_samples)
sobol_engine = torch.quasirandom.SobolEngine(dim, seed=1)
seeded_samples = sobol_engine.draw(num_samples)