'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quasirandom.SobolEngine\ntorch.quasirandom.SobolEngine(dimension, scramble=False, seed=None)\n'
import torch
import numpy as np
import torch
import numpy as np
n = 100
d = 3
x = np.random.rand(n, d)
sobol_engine = torch.quasirandom.SobolEngine(d)
samples = sobol_engine.draw(n)
print(samples)
print(samples.shape)