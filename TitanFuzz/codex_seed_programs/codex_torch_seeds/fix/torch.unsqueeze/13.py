'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
input_data = torch.randn(1, 2, 3)
print('Input data: ', input_data)
print('Input data shape: ', input_data.shape)
output_data = torch.unsqueeze(input_data, 0)
print('Output data: ', output_data)
print('Output data shape: ', output_data.shape)