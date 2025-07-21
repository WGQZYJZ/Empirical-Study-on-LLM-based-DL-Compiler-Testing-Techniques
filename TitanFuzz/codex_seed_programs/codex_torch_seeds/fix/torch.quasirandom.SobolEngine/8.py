'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quasirandom.SobolEngine\ntorch.quasirandom.SobolEngine(dimension, scramble=False, seed=None)\n'
import torch
dimension = 2
scramble = False
seed = None
sobol_engine = torch.quasirandom.SobolEngine(dimension, scramble, seed)
print('SobolEngine: ', sobol_engine)
print('SobolEngine.draw(4): ', sobol_engine.draw(4))
print('SobolEngine.draw(4): ', sobol_engine.draw(4))