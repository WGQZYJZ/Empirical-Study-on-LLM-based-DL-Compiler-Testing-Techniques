'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isposinf\ntorch.isposinf(input, *, out=None)\n'
import torch
input = torch.randn(1, 1)
output = torch.isposinf(input)
print('Input: ', input)
print('Output: ', output)