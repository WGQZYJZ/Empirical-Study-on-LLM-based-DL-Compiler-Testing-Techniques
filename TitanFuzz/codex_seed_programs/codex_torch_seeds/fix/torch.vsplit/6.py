'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vsplit\ntorch.vsplit(input, indices_or_sections)\n'
import torch
input_tensor = torch.randn(4, 6)
print('input_tensor: ', input_tensor)
output_tensor = torch.vsplit(input_tensor, 2)
print('output_tensor: ', output_tensor)