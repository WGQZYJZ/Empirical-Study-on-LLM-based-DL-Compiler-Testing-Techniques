'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmin\ntorch.argmin(input, dim=None, keepdim=False)\n'
import torch
input = torch.randn(10, 3)
print('Input: ', input)
index = torch.argmin(input, dim=1)
print('index: ', index)
print('min value: ', input[(range(input.size(0)), index)])