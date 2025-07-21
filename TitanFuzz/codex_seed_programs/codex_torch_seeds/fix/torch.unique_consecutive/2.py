'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique_consecutive\ntorch.unique_consecutive(input, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input_data = torch.tensor([1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 9, 10, 10])
input_data = input_data.unsqueeze(0)
print('Input data: ', input_data)
print('Input data shape: ', input_data.shape)
output_data = torch.unique_consecutive(input_data)
print('Output data: ', output_data)
print('Output data shape: ', output_data.shape)