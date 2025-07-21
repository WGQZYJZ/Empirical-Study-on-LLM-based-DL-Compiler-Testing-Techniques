'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log\ntorch.log(input, *, out=None)\n'
import torch
input = torch.randn(1, 1)
print('Input: ', input)
output = torch.log(input)
print('Output: ', output)