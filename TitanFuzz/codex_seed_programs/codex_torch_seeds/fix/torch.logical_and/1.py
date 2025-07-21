'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_and\ntorch.logical_and(input, other, *, out=None)\n'
import torch
input = torch.Tensor([[1, 0, 1], [1, 0, 0]])
other = torch.Tensor([[0, 0, 1], [1, 0, 1]])
print(torch.logical_and(input, other))