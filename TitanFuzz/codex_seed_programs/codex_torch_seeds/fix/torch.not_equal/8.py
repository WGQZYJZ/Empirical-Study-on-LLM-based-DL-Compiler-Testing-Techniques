'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.not_equal\ntorch.not_equal(input, other, *, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4])
y = torch.tensor([3, 4, 5, 6])
z = torch.not_equal(x, y)
print('z = ', z)
x = torch.rand(3, 3)
print('x = ', x)
y = torch.not_equal(x, x)
print('y = ', y)