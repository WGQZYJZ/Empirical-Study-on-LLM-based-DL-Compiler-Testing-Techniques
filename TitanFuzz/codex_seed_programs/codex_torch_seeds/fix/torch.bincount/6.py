'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bincount\ntorch.bincount(input, weights=None, minlength=0)\n'
import torch
input = torch.tensor([1, 2, 3, 4, 5, 6, 6, 6])
print(torch.bincount(input))
print(torch.bincount(input, minlength=10))
weights = torch.tensor([0.3, 0.5, 0.2, 0.7, 0.1, 0.2, 0.3, 0.3])
print(torch.bincount(input, weights=weights))
print(torch.bincount(input, weights=weights, minlength=10))