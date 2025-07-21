'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frac\ntorch.frac(input, *, out=None)\n'
import torch
input = torch.randn(1, 3, 3)
output = torch.frac(input, out=None)
print('input:')
print(input)
print('output:')
print(output)