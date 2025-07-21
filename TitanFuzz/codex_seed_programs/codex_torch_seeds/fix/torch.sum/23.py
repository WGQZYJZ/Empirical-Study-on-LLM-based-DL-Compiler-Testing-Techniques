'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sum\ntorch.sum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
x = torch.Tensor([[1, 2, 3], [4, 5, 6]])
print(torch.sum(x, dim=0))
print(torch.sum(x, dim=1))
print(torch.sum(x, dim=1, keepdim=True))
print(torch.sum(x, dim=1, keepdim=True).shape)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mean\ntorch.mean(input, dim, keepdim=False, *, dtype=None)\n'
import torch
x = torch.Tensor([[1, 2, 3], [4, 5, 6]])
print(torch.mean(x, dim=0))
print(torch.mean(x, dim=1))