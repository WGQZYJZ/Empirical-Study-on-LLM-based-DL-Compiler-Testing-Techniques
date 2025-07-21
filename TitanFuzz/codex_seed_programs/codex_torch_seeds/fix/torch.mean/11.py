'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mean\ntorch.mean(input, dim, keepdim=False, *, dtype=None)\n'
import torch
import torch
input = torch.randn(4, 3)
mean_value = torch.mean(input)
print(mean_value)