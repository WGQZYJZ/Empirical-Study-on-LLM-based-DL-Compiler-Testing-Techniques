'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quasirandom.SobolEngine\ntorch.quasirandom.SobolEngine(dimension, scramble=False, seed=None)\n'
import torch
sobol_engine = torch.quasirandom.SobolEngine(dimension=2)
print(sobol_engine.draw(2))
sobol_engine = torch.quasirandom.SobolEngine(dimension=3)
print(sobol_engine.draw(2))
sobol_engine = torch.quasirandom.SobolEngine(dimension=4)
print(sobol_engine.draw(2))
sobol_engine = torch.quasirandom.SobolEngine(dimension=5)
print(sobol_engine.draw(2))
sobol_engine = torch.quasirandom.SobolEngine(dimension=6)