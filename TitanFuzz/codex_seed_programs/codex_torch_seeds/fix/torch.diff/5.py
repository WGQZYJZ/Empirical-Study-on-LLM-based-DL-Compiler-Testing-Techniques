'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diff\ntorch.diff(input, n=1, dim=-1, prepend=None, append=None)\n'
import torch
x = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(x)
print(torch.diff(x))
print(torch.diff(x, n=2))
print(torch.diff(x, n=1, dim=0))
print(torch.diff(x, n=1, dim=1))