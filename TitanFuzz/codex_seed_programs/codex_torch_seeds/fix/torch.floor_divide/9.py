'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5, 6])
y = torch.tensor([2, 2, 2, 2, 2, 2])
z = torch.floor_divide(x, y)
print('The result of floor_divide: ', z)