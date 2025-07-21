'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique\ntorch.unique(input, sorted=True, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input = torch.tensor([1, 3, 2, 3])
print(input)
result = torch.unique(input)
print(result)
result = torch.unique(input, sorted=True, return_inverse=True, return_counts=True)
print(result)