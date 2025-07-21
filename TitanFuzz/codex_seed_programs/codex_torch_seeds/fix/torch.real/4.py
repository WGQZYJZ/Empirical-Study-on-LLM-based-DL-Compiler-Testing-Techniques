'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.real\ntorch.real(input)\n'
import torch
input_data = torch.rand(3, 3)
print('Input data: ', input_data)
output_data = torch.real(input_data)
print('Output data: ', output_data)