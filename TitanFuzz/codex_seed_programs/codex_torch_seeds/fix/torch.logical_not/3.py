'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_not\ntorch.logical_not(input, *, out=None)\n'
import torch
x = torch.tensor([True, False])
y = torch.logical_not(x)
print('Input: ', x)
print('Output: ', y)