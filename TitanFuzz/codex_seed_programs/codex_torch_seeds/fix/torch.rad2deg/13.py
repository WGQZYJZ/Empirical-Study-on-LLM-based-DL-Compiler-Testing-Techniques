'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rad2deg\ntorch.rad2deg(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 4)
output_data = torch.rad2deg(input_data)
print('Input data:\n', input_data)
print('Output data:\n', output_data)