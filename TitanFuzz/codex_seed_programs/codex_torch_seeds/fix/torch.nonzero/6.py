'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nonzero\ntorch.nonzero(input, *, out=None, as_tuple=False)\n'
import torch
x = torch.tensor([[1, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]])
print('x = ', x)
print('torch.nonzero(x) = ', torch.nonzero(x))
print('torch.nonzero(x, as_tuple=True) = ', torch.nonzero(x, as_tuple=True))