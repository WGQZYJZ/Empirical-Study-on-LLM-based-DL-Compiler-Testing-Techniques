'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vsplit\ntorch.vsplit(input, indices_or_sections)\n'
import torch
input_data = torch.arange(9, dtype=torch.float).reshape(3, 3)
print('Input data: ', input_data)
output_data = torch.vsplit(input_data, [1, 2])
print('Output data: ', output_data)
output_data = torch.vsplit(input_data, [1])
print('Output data: ', output_data)