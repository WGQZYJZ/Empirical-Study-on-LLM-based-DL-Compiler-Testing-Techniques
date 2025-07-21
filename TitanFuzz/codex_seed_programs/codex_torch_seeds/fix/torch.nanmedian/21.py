'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanmedian\ntorch.nanmedian(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(4, 4)
input[(1, 1)] = float('nan')
input[(2, 2)] = float('nan')
input[(3, 3)] = float('nan')
print('Input data: \n', input)
print('Median of input data: \n', torch.nanmedian(input))
print('Median of input data along dimension 0: \n', torch.nanmedian(input, dim=0))
print('Median of input data along dimension 1: \n', torch.nanmedian(input, dim=1))
print('Median of input data along dimension 1 with keepdim: \n', torch.nanmedian(input, dim=1, keepdim=True))