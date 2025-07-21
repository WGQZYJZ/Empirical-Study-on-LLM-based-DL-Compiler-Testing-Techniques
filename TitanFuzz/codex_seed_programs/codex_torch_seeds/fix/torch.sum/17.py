'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sum\ntorch.sum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(x)
y = torch.sum(x, dim=0)
print(y)
y = torch.sum(x, dim=1)
print(y)
y = torch.sum(x, dim=1, keepdim=True)
print(y)