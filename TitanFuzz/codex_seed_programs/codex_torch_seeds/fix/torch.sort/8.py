'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sort\ntorch.sort(input, dim=-1, descending=False, stable=False, *, out=None)\n'
import torch
input_data = torch.randn(10, 3)
(sorted_data, sorted_indices) = torch.sort(input_data)
print(sorted_data)
print(sorted_indices)