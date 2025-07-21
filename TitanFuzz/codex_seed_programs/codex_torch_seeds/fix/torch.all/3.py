'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.all\ntorch.all(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input: ', input)
output = torch.all(input)
print('Output: ', output)