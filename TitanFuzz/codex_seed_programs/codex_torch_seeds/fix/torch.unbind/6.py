'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unbind\ntorch.unbind(input, dim=0)\n'
import torch
input = torch.rand(2, 3)
print('Input data: ', input)
output = torch.unbind(input, dim=0)
print('Output data: ', output)