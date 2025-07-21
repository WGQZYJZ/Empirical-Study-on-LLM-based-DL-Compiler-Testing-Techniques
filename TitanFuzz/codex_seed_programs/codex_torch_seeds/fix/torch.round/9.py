'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
input_data = torch.tensor([0.9, 0.4, 0.2, 0.3, 0.7, 0.1, 0.8, 0.5])
output_data = torch.round(input_data)
print('Input data: {}'.format(input_data))
print('Output data: {}'.format(output_data))