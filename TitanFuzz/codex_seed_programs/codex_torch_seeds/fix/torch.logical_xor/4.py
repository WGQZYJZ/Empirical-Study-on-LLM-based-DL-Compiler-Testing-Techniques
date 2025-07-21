'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_xor\ntorch.logical_xor(input, other, *, out=None)\n'
import torch
x = torch.tensor([True, True, False, False], dtype=torch.bool)
y = torch.tensor([True, False, True, False], dtype=torch.bool)
z = torch.logical_xor(x, y)
print('The result of logical_xor of x and y is {}'.format(z))