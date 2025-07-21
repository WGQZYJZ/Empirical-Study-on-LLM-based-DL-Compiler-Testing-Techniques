'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumsum\ntorch.cumsum(input, dim, *, dtype=None, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('Input data: ', x)
y = torch.cumsum(x, dim=0)
print('Output data: ', y)