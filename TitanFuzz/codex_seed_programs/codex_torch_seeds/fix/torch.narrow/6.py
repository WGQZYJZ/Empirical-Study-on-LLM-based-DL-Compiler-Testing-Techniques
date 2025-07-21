'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.narrow\ntorch.narrow(input, dim, start, length)\n'
import torch
input_data = torch.arange(1, 11)
output_data = torch.narrow(input_data, 0, 1, 4)
print('input data: {}'.format(input_data))
print('output data: {}'.format(output_data))