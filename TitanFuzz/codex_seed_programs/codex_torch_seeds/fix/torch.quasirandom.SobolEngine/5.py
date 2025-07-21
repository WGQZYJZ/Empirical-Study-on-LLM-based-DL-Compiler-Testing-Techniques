'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quasirandom.SobolEngine\ntorch.quasirandom.SobolEngine(dimension, scramble=False, seed=None)\n'
import torch
import torch
x = torch.randn(10000, 2)
engine = torch.quasirandom.SobolEngine(2)
quasi_random_numbers = engine.draw(10000)
print('x: \n', x)
print('quasi_random_numbers: \n', quasi_random_numbers)