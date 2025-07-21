'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique\ntorch.unique(input, sorted=True, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input_data = torch.tensor([1, 3, 2, 3, 4, 2])
(unique_data, inverse_data, counts_data) = torch.unique(input_data, sorted=True, return_inverse=True, return_counts=True, dim=None)
print('Input data: ', input_data)
print('Unique data: ', unique_data)
print('Inverse data: ', inverse_data)
print('Counts data: ', counts_data)