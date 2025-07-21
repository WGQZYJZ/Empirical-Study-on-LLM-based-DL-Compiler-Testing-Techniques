'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantile\ntorch.quantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print('input: ', input)
q = 0.5
dim = 0
keepdim = True
out = torch.quantile(input, q, dim, keepdim)
print('out: ', out)