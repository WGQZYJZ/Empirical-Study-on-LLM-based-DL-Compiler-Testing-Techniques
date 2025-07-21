'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccosh\ntorch.arccosh(input, *, out=None)\n'
import torch
input = torch.tensor([1.0, 2.0, 3.0])
print('Input: ', input)
output = torch.arccosh(input)
print('Output: ', output)