'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nan_to_num\ntorch.nan_to_num(input, nan=0.0, posinf=None, neginf=None, *, out=None)\n'
import torch
input = torch.randn(4, 4)
input[(0, 0)] = float('nan')
input[(1, 1)] = float('inf')
input[(2, 2)] = float('-inf')
print('Input data: \n', input)
output = torch.nan_to_num(input)
print('Output data: \n', output)