'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i0\ntorch.special.i0(input, *, out=None)\n'
import torch
import math
import torch
input = torch.randn(4, 4)
output = torch.special.i0(input)
print('input: \n', input)
print('output: \n', output)