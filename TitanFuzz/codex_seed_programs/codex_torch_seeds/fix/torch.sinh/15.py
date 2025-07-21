'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sinh\ntorch.sinh(input, *, out=None)\n'
import torch
input = torch.randn(1, 3)
print('Input: ', input)
output = torch.sinh(input)
print('Output: ', output)