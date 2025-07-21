'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vsplit\ntorch.vsplit(input, indices_or_sections)\n'
import torch
import torch
input = torch.rand(4, 3, 2)
print('Input:\n', input)
print('\nOutput:\n', torch.vsplit(input, 2))