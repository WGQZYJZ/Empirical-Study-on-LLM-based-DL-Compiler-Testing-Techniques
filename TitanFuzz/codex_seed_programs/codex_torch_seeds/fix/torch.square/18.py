'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.square\ntorch.square(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3, 4)
print('Input data: {}'.format(input_data))
output_data = torch.square(input_data)
print('Output data: {}'.format(output_data))