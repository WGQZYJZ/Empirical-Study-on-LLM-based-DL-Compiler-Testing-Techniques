'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.erfinv\ntorch.special.erfinv(input, *, out=None)\n'
import torch
import torch
input = torch.randn(4)
print('input: ', input)
output = torch.special.erfinv(input)
print('output: ', output)