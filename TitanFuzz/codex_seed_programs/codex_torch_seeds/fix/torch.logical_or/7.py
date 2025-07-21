'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_or\ntorch.logical_or(input, other, *, out=None)\n'
import torch
x = torch.tensor([[True, False], [True, True]])
y = torch.tensor([[False, False], [True, False]])
z = torch.logical_or(x, y)
print(z)
'\nTask 4: Call the API torch.logical_and\ntorch.logical_and(input, other, *, out=None)\n'
x = torch.tensor([[True, False], [True, True]])
y = torch.tensor([[False, False], [True, False]])
z = torch.logical_and(x, y)
print(z)
'\nTask 5: Call the API torch.logical_xor\ntorch.logical_xor(input, other, *, out=None)\n'
x = torch.tensor([[True, False], [True, True]])
y = torch.tensor([[False, False], [True, False]])
z = torch.logical_xor(x, y)