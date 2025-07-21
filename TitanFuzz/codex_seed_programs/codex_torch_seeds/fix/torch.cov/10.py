'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cov\ntorch.cov(input, *, correction=1, fweights=None, aweights=None)\n'
import torch
import torch
input = torch.randn(3, 3)
print(input)
output = torch.cov(input)
print(output)