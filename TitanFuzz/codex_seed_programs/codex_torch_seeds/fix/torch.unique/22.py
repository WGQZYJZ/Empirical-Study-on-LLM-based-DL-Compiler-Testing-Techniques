'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique\ntorch.unique(input, sorted=True, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input_data = torch.tensor([[1, 3, 3], [2, 2, 1], [3, 1, 1]])
(unique_data, inverse_data, counts_data) = torch.unique(input_data, sorted=True, return_inverse=True, return_counts=True, dim=0)
print('input_data: ', input_data)
print('unique_data: ', unique_data)
print('inverse_data: ', inverse_data)
print('counts_data: ', counts_data)