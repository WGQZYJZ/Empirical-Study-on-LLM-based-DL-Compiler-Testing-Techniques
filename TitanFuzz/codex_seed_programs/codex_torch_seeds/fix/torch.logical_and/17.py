'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_and\ntorch.logical_and(input, other, *, out=None)\n'
import torch
x = torch.tensor([[True, False], [True, True]])
y = torch.tensor([[False, False], [True, False]])
print(torch.logical_and(x, y))