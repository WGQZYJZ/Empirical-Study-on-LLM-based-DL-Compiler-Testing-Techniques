'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.all\ntorch.all(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(2, 3)
print('Input: ', input)
print('torch.all(input): ', torch.all(input))
input = torch.randn(2, 3)
print('Input: ', input)
print('torch.all(input, dim=0): ', torch.all(input, dim=0))
input = torch.randn(2, 3)
print('Input: ', input)
print('torch.all(input, dim=1): ', torch.all(input, dim=1))
input = torch.randn(2, 3)
print('Input: ', input)
print('torch.all(input, dim=1, keepdim=True): ', torch.all(input, dim=1, keepdim=True))