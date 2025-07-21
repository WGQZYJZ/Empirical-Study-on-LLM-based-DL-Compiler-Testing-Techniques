'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.min\ntorch.min(input, dim, keepdim=False, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('PyTorch version:', torch.__version__)
print('\nTask 2: Generate input data')
x = torch.rand(2, 3)
print('x:', x)
print('\nTask 3: Call the API torch.min')
print('torch.min(x, dim=0):', torch.min(x, dim=0))
print('torch.min(x, dim=1):', torch.min(x, dim=1))
print('torch.min(x, dim=0, keepdim=True):', torch.min(x, dim=0, keepdim=True))
print('torch.min(x, dim=1, keepdim=True):', torch.min(x, dim=1, keepdim=True))