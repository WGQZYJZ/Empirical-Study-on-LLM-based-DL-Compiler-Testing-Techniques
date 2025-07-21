'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vsplit\ntorch.vsplit(input, indices_or_sections)\n'
import torch
import torch
input_data = torch.arange(start=0, end=16, dtype=torch.float).view(4, 4)
output_data = torch.vsplit(input_data, 2)
print('The input data is:')
print(input_data)
print('The output data is:')
print(output_data)