'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quasirandom.SobolEngine\ntorch.quasirandom.SobolEngine(dimension, scramble=False, seed=None)\n'
import torch
dim = 5
sobol_engine = torch.quasirandom.SobolEngine(dim)
print(sobol_engine.draw(5))
print(sobol_engine.draw(5))
print(sobol_engine.draw(5))
print(sobol_engine.draw(5))
print(sobol_engine.draw(5))
print(sobol_engine.draw(5))