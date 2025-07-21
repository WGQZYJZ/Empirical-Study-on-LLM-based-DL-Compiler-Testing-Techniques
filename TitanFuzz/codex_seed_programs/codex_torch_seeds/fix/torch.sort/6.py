'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sort\ntorch.sort(input, dim=-1, descending=False, stable=False, *, out=None)\n'
import torch
import torch
input_data = torch.rand(4, 3)
print('Input data:', input_data)
(sorted_data, sorted_indices) = torch.sort(input_data)
print('Sorted data:', sorted_data)
print('Sorted indices:', sorted_indices)
(sorted_data, sorted_indices) = torch.sort(input_data, dim=1)
print('Sorted data:', sorted_data)
print('Sorted indices:', sorted_indices)
(sorted_data, sorted_indices) = torch.sort(input_data, dim=1, descending=True)
print('Sorted data:', sorted_data)
print('Sorted indices:', sorted_indices)
(sorted_data, sorted)