'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.histogram\ntorch.histogram(input, bins, *, range=None, weight=None, density=False, out=None)\n'
import torch
input = torch.rand(1000)
histogram = torch.histogram(input, bins=10, range=(0, 1))
print(histogram)