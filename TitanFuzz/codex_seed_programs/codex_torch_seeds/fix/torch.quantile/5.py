'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantile\ntorch.quantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 4)
print('Input:\n', input)
q = torch.quantile(input, 0.5, dim=0)
print('Quantile of the input along dim=0:\n', q)
q = torch.quantile(input, 0.5, dim=1, keepdim=True)
print('Quantile of the input along dim=1:\n', q)
q = torch.quantile(input, 0.5, dim=(- 1), keepdim=True)
print('Quantile of the input along dim=-1:\n', q)
q = torch.quantile(input, 0.5, dim=None)
print('Quantile of the input along dim=None:\n', q)
out = torch.empty(3)