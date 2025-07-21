'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bincount\ntorch.bincount(input, weights=None, minlength=0)\n'
import torch
input = torch.randint(0, 10, (10,))
print(input)
counts = torch.bincount(input)
print(counts)
weights = torch.rand(10)
print(weights)
counts = torch.bincount(input, weights)
print(counts)
counts = torch.bincount(input, weights, minlength=10)
print(counts)