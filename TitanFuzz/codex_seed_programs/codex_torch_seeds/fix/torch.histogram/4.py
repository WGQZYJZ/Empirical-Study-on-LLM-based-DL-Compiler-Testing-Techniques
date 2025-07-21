'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.histogram\ntorch.histogram(input, bins, *, range=None, weight=None, density=False, out=None)\n'
import torch
import torch
input = torch.randn(100000, dtype=torch.float32)
hist = torch.histogram(input, bins=10, range=((- 3), 3))
print(hist)
print(hist[0])
print(hist[1])
hist = torch.histogram(input, bins=10, range=((- 3), 3), density=True)
print(hist)
print(hist[0])
print(hist[1])