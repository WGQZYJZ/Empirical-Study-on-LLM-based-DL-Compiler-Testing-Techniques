'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.histogram\ntorch.histogram(input, bins, *, range=None, weight=None, density=False, out=None)\n'
import torch
import torch
input = torch.rand(10)
bins = 3
histogram = torch.histogram(input, bins)
print('histogram: ', histogram)