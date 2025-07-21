'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vsplit\ntorch.vsplit(input, indices_or_sections)\n'
import torch
input = torch.randn(2, 3, 5)
print('Input data is: ', input)
output = torch.vsplit(input, 2)
print('Output data is: ', output)