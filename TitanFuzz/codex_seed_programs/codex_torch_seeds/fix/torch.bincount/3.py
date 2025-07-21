'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bincount\ntorch.bincount(input, weights=None, minlength=0)\n'
import torch
input = torch.tensor([2, 3, 1, 2, 0, 2, 3, 1, 2, 0, 0, 2, 3, 3, 1, 2, 0, 2, 3, 1, 2, 0, 0, 2, 3, 3])
weights = torch.tensor([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
print(torch.bincount(input, weights=weights, minlength=4))