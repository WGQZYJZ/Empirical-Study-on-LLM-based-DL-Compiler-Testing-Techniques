'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.abs\ntorch.abs(input, *, out=None)\n'
import torch
input_data = torch.rand(3, 5)
print('Input data is: ', input_data)
output_data = torch.abs(input_data)
print('Output data is: ', output_data)