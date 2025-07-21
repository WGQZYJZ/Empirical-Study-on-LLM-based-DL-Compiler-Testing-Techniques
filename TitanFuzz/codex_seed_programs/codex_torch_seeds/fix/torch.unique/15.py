'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique\ntorch.unique(input, sorted=True, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input_data = torch.tensor([1, 3, 2, 3])
(unique_data, inverse_data, counts_data) = torch.unique(input_data, sorted=True, return_inverse=True, return_counts=True)
print('Input data is: {}'.format(input_data))
print('Unique data is: {}'.format(unique_data))
print('Inverse data is: {}'.format(inverse_data))
print('Counts data is: {}'.format(counts_data))
'\nTask 4: Generate input data\nTask 5: Call the API torch.unique\ntorch.unique(input, sorted=True, return_inverse=False, return_counts=False, dim=None)\n'
input_data_2 = torch.tensor([[1, 3, 2, 3], [1, 3, 2, 3]])