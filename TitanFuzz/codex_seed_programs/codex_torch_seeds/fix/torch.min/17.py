'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.min\ntorch.min(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(4, 4)
output = torch.min(input, 1)
print(output)