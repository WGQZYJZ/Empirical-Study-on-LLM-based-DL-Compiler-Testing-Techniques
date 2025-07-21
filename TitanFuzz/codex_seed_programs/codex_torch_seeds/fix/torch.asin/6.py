'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.asin\ntorch.asin(input, *, out=None)\n'
import torch
input = torch.randn(1, 1, 3)
print('Input: ', input)
output = torch.asin(input)
print('Output: ', output)