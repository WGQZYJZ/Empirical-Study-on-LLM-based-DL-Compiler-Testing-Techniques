'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bincount\ntorch.bincount(input, weights=None, minlength=0)\n'
import torch
input = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
weights = torch.tensor([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
print(torch.bincount(input, weights=weights))
print(torch.bincount(input, weights=weights, minlength=15))