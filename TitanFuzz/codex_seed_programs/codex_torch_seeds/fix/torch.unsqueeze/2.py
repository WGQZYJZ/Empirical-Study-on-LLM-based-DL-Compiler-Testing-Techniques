'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
import torch
input_data = torch.randn(2, 3)
print('Input data: \n', input_data)
print('Input data shape: \n', input_data.shape)
output_data = torch.unsqueeze(input_data, dim=0)
print('Output data: \n', output_data)
print('Output data shape: \n', output_data.shape)