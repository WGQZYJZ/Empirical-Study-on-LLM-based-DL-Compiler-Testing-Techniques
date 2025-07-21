'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cos\ntorch.cos(input, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print(input)
print(torch.cos(input))