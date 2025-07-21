'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ceil\ntorch.ceil(input, *, out=None)\n'
import torch
data = torch.randn(1, 2, 3, 4)
print('input data: \n', data)
print('after torch.ceil: \n', torch.ceil(data))