'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quasirandom.SobolEngine\ntorch.quasirandom.SobolEngine(dimension, scramble=False, seed=None)\n'
import torch
dimension = 10
scramble = False
seed = None
sobol_engine = torch.quasirandom.SobolEngine(dimension, scramble, seed)
print(sobol_engine)
print(sobol_engine.draw(5))