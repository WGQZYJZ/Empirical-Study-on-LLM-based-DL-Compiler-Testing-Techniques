'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.std\ntorch.std(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(1, 3)
print(input)
std = torch.std(input)
print(std)