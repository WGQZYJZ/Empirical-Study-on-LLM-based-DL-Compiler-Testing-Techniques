'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.max\ntorch.max(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 5)
print(input)
print('\n')
(max_value, max_idx) = torch.max(input, dim=0)
print(max_value)
print(max_idx)
print('\n')
(max_value, max_idx) = torch.max(input, dim=1)
print(max_value)
print(max_idx)