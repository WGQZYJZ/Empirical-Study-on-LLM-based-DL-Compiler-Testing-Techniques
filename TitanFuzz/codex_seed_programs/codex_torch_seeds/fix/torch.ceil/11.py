'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ceil\ntorch.ceil(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print('Input data is: ', input_data)
output_data = torch.ceil(input_data)
print('Output data is: ', output_data)