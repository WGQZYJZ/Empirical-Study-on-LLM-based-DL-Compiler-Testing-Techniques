'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sort\ntorch.sort(input, dim=-1, descending=False, stable=False, *, out=None)\n'
import torch
input = torch.randn(3, 5)
print('Input data:', input)
(sorted_data, sorted_indices) = torch.sort(input)
print('Sorted data:', sorted_data)
print('Sorted indices:', sorted_indices)
(sorted_data, sorted_indices) = torch.sort(input, dim=0)
print('Sorted data:', sorted_data)
print('Sorted indices:', sorted_indices)
(sorted_data, sorted_indices) = torch.sort(input, dim=1)
print('Sorted data:', sorted_data)
print('Sorted indices:', sorted_indices)