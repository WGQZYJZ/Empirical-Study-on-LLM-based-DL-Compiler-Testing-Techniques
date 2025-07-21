'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.erfinv\ntorch.special.erfinv(input, *, out=None)\n'
import torch
input_data = torch.rand(1, 2)
print('Input data: {}'.format(input_data))
output_data = torch.special.erfinv(input_data)
print('Output data: {}'.format(output_data))