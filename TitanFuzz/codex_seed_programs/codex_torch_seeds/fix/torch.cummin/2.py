'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cummin\ntorch.cummin(input, dim, *, out=None)\n'
import torch
input = torch.randn(10, 10)
print('Input:', input)
print('\nCummin along axis 0:', torch.cummin(input, dim=0))
print('\nCummin along axis 1:', torch.cummin(input, dim=1))