'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, *, out=None)\n'
import torch
input_data = torch.randn(1, 3, 3, 1)
print('Input data:\n', input_data)
output_data = torch.squeeze(input_data, dim=(- 1))
print('Output data:\n', output_data)
output_data = torch.squeeze(input_data, dim=1)
print('Output data:\n', output_data)