'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cross\ntorch.cross(input, other, dim=None, *, out=None)\n'
import torch
a = torch.tensor([[1, 2, 3], [4, 5, 6]])
b = torch.tensor([[1, 1, 1], [2, 2, 2]])
c = torch.cross(a, b)
print(c)
c = torch.cross(a, b, dim=1)
print(c)