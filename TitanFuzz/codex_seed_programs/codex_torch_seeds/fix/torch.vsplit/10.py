'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vsplit\ntorch.vsplit(input, indices_or_sections)\n'
import torch
input_data = torch.arange(start=0, end=16, dtype=torch.float32).view(4, 4)
print('Input data:', input_data)
output = torch.vsplit(input_data, 2)
print('Output:', output)