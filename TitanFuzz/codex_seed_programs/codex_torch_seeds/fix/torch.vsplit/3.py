'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vsplit\ntorch.vsplit(input, indices_or_sections)\n'
import torch
x = torch.arange(16, dtype=torch.float32).reshape(2, 8)
print('Input data: \n', x)
y = torch.vsplit(x, 2)
print('Output data: \n', y)