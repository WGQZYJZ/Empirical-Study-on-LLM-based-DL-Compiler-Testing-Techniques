'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.var_mean\ntorch.var_mean(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(4, 4)
print(input)
print(torch.var_mean(input, 1, True))