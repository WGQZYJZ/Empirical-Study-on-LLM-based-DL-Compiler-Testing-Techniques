'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.moveaxis\ntorch.moveaxis(input, source, destination)\n'
import torch
input_data = torch.randn(3, 4, 5)
print('input_data: ', input_data)
print('input_data.shape: ', input_data.shape)
output_data = torch.moveaxis(input_data, 0, 1)
print('output_data: ', output_data)
print('output_data.shape: ', output_data.shape)
output_data = torch.moveaxis(input_data, 0, 2)
print('output_data: ', output_data)
print('output_data.shape: ', output_data.shape)
output_data = torch.moveaxis(input_data, 1, 0)
print('output_data: ', output_data)
print('output_data.shape: ', output_data.shape)
output_data = torch.moveaxis