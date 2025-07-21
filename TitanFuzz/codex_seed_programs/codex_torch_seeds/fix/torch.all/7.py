'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.all\ntorch.all(input, dim, keepdim=False, *, out=None)\n'
import torch
a = torch.tensor([[True, False], [False, False]])
b = torch.tensor([[True, True], [True, True]])
c = torch.tensor([[False, False], [False, False]])
print('torch.all(input)')
print('torch.all(a) = ', torch.all(a))
print('torch.all(b) = ', torch.all(b))
print('torch.all(c) = ', torch.all(c))
print('\ntorch.all(input, dim, keepdim=False)')
print('torch.all(a, 1) = ', torch.all(a, 1))
print('torch.all(b, 1) = ', torch.all(b, 1))
print('torch.all(c, 1) = ', torch.all(c, 1))