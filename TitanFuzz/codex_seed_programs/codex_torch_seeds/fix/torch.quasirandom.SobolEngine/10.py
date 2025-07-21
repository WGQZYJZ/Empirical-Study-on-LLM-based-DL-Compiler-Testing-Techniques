'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quasirandom.SobolEngine\ntorch.quasirandom.SobolEngine(dimension, scramble=False, seed=None)\n'
import torch
input = torch.rand(5, 4)
print('Input: ', input)
input_sobol = torch.quasirandom.SobolEngine(4).draw(5)
print('Sobol Sequence: ', input_sobol)