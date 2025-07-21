'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique\ntorch.unique(input, sorted=True, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input = torch.tensor([1, 3, 2, 3, 4, 3])
print(torch.unique(input))
print(torch.unique(input, sorted=True))
print(torch.unique(input, return_inverse=True))
print(torch.unique(input, return_counts=True))
input = torch.tensor([[1, 3, 2, 3, 4, 3], [1, 3, 2, 3, 4, 3]])
print(torch.unique(input, dim=0))
input = torch.tensor([[1, 3, 2, 3, 4, 3], [1, 3, 2, 3, 4, 3]])
print(torch.unique(input, dim=1))