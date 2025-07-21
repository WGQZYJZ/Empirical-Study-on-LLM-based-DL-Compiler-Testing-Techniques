'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.max\ntorch.max(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(10, 5)
print(input_data)
(max_value, max_idx) = torch.max(input_data, dim=1)
print(max_value)
print(max_idx)
(max_value, max_idx) = torch.max(input_data, dim=1, keepdim=True)
print(max_value)
print(max_idx)
(max_value, max_idx) = torch.max(input_data, dim=0, keepdim=True)
print(max_value)
print(max_idx)