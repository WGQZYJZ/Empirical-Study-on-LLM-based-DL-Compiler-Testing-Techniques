'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sigmoid\ntorch.sigmoid(input, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input: ', input)
output = torch.sigmoid(input)
print('Output: ', output)