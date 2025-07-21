'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.asin\ntorch.asin(input, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print('Input: ', input)
out = torch.asin(input)
print('Output: ', out)