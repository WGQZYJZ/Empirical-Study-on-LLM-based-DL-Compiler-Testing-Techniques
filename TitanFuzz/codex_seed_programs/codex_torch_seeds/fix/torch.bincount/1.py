'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bincount\ntorch.bincount(input, weights=None, minlength=0)\n'
import torch
import torch
input = torch.tensor([1, 1, 2, 3, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8, 8, 8, 9, 10, 10])
torch.bincount(input)
weights = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
torch.bincount(input, weights=weights)