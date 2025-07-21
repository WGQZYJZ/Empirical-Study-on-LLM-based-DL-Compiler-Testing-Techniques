'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.min\ntorch.min(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print(input)
(min_value, min_index) = torch.min(input, dim=1)
print(min_value)
print(min_index)