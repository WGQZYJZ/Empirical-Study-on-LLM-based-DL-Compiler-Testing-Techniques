'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.absolute\ntorch.absolute(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 3)
print('Input data: ', input_data)
output_data = torch.absolute(input_data)
print('Output data: ', output_data)