'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantile\ntorch.quantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(2, 3)
print('input: ', input)
quantile = torch.quantile(input, 0.5, dim=1, keepdim=True)
print('quantile: ', quantile)