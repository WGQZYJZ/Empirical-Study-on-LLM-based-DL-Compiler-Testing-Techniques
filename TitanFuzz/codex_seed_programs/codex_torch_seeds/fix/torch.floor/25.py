'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor\ntorch.floor(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print('Input Data:', input_data)
output_data = torch.floor(input_data)
print('Output Data:', output_data)