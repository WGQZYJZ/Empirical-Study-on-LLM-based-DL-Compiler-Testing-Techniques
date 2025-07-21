'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quasirandom.SobolEngine\ntorch.quasirandom.SobolEngine(dimension, scramble=False, seed=None)\n'
import torch
dimension = 5
sobol_engine = torch.quasirandom.SobolEngine(dimension)
print(sobol_engine)
print(sobol_engine.draw())
print(sobol_engine.draw())