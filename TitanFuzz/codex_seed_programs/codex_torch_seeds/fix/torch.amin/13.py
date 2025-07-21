'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amin\ntorch.amin(input, dim, keepdim=False, *, out=None)\n'
import torch
data = torch.randn(2, 3)
print('Input data: \n', data)
print('\nMinimum value along the first dimension: \n', torch.amin(data, dim=0))
print('\nMinimum value along the second dimension: \n', torch.amin(data, dim=1))