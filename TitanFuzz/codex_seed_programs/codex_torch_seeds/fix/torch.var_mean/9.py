'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.var_mean\ntorch.var_mean(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(2, 3)
print('input = ', input)
print('torch.var_mean(input, dim=1) = ', torch.var_mean(input, dim=1))