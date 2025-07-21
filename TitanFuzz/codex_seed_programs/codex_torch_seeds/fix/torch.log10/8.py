'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log10\ntorch.log10(input, *, out=None)\n'
import torch
input_data = torch.arange(1, 11, dtype=torch.float32)
print('Input data: ', input_data)
output_data = torch.log10(input_data)
print('Output data: ', output_data)