'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sort\ntorch.sort(input, dim=-1, descending=False, stable=False, *, out=None)\n'
import torch
import torch
data = torch.randn(2, 3, 4)
print(data)
(sorted_data, sorted_indices) = torch.sort(data)
print(sorted_data)
print(sorted_indices)
(sorted_data, sorted_indices) = torch.sort(data, dim=1)
print(sorted_data)
print(sorted_indices)
(sorted_data, sorted_indices) = torch.sort(data, dim=2)
print(sorted_data)
print(sorted_indices)