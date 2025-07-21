'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frac\ntorch.frac(input, *, out=None)\n'
import torch
input = torch.randn(5, 5)
output = torch.frac(input)
print('Input: ', input)
print('Output: ', output)