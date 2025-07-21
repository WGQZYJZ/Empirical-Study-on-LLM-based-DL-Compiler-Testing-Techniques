'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chunk\ntorch.chunk(input, chunks, dim=0)\n'
import torch
import torch
input_data = torch.randn(4, 4)
print('Input data: ', input_data)
output_data = torch.chunk(input_data, 2, dim=0)
print('Output data: ', output_data)
print('Output data: ', output_data[0])
print('Output data: ', output_data[1])
output_data = torch.chunk(input_data, 2, dim=1)
print('Output data: ', output_data)
print('Output data: ', output_data[0])
print('Output data: ', output_data[1])