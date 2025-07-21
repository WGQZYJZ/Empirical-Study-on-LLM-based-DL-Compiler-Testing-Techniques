'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.polygamma\ntorch.polygamma(n, input, *, out=None)\n'
import torch
n = 3
input = torch.randn(2, 3)
print(torch.polygamma(n, input))