'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.max\ntorch.max(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 5)
print('input:', input)
(max_value, max_index) = torch.max(input, dim=1, keepdim=False)
print('max_value:', max_value)
print('max_index:', max_index)
max_value