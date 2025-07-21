'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bincount\ntorch.bincount(input, weights=None, minlength=0)\n'
import torch
input = torch.tensor([2, 3, 9, 2, 5, 9, 9, 2, 4, 2])
print(torch.bincount(input))
print(torch.bincount(input, minlength=10))