'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frac\ntorch.frac(input, *, out=None)\n'
import torch
input = torch.rand(2, 3)
print('Input: ', input)
frac_output = torch.frac(input)
print('Output: ', frac_output)