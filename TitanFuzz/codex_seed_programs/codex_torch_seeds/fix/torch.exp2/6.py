'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp2\ntorch.exp2(input, *, out=None)\n'
import torch
input = torch.randn(1)
print('input: ', input)
output = torch.exp2(input)
print('output: ', output)