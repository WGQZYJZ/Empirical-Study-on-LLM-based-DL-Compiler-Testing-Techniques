'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 1, 3, 3)
print('Input Data: ', input_data)
output_data = torch.round(input_data)
print('Output Data: ', output_data)