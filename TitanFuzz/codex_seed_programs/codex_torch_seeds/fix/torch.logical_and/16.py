'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_and\ntorch.logical_and(input, other, *, out=None)\n'
import torch
input = torch.tensor([[1, 0, 1, 1], [1, 0, 1, 1]])
other = torch.tensor([[1, 1, 1, 0], [0, 0, 1, 1]])
out = torch.logical_and(input, other)
print(out)