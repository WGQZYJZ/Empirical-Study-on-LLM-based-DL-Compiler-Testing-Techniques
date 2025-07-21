'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_and\ntorch.logical_and(input, other, *, out=None)\n'
import torch
a = torch.tensor([True, False, False, True])
b = torch.tensor([False, False, True, True])
result = torch.logical_and(a, b)
print(result)