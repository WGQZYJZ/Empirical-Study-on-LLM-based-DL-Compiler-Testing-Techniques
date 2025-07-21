'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanquantile\ntorch.nanquantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
input_data = torch.rand(5, 5)
print('input_data: ', input_data)
quantile = torch.nanquantile(input_data, 0.5, dim=None, keepdim=False, out=None)
print('quantile: ', quantile)