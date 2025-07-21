'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bincount\ntorch.bincount(input, weights=None, minlength=0)\n'
import torch
input = torch.LongTensor([1, 2, 3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])
weights = torch.FloatTensor([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
print(torch.bincount(input))
print(torch.bincount(input, weights=weights))