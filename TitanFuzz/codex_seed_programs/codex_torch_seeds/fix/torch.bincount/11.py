'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bincount\ntorch.bincount(input, weights=None, minlength=0)\n'
import torch
input = torch.tensor([1, 2, 2, 4, 5, 4, 4, 4])
torch.bincount(input)
torch.bincount(input, minlength=10)
weights = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
torch.bincount(input, weights=weights)
torch.bincount(input, weights=weights, minlength=10)