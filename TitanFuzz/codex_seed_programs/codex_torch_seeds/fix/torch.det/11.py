'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.det\ntorch.det(input)\n'
import torch
input = torch.randn(3, 3)
print('Input data: ', input)
output = torch.det(input)
print('Output data: ', output)