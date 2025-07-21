'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rad2deg\ntorch.rad2deg(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 3, 5)
output_data = torch.rad2deg(input_data)
print('input_data: ', input_data)
print('output_data: ', output_data)
'\nQuestion:\n1. What is the difference between torch.deg2rad and torch.rad2deg?\n2. Can you use torch.deg2rad to convert the output_data back to the input_data?\n'