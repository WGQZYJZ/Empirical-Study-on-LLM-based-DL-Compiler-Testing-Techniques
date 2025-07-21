'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.narrow\ntorch.narrow(input, dim, start, length)\n'
import torch
input_data = torch.arange(1, 9)
print('Input data: ', input_data)
input_data = torch.arange(1, 9)
print('Input data: ', input_data)
output_data = torch.narrow(input_data, dim=0, start=0, length=4)
print('Output data: ', output_data)