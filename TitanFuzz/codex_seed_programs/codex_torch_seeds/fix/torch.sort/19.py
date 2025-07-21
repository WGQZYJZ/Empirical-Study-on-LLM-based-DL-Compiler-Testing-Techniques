'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sort\ntorch.sort(input, dim=-1, descending=False, stable=False, *, out=None)\n'
import torch
input = torch.randn(3, 5)
print(input)
(sorted_input, sorted_indices) = torch.sort(input)
print(sorted_input)
print(sorted_indices)