'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trace\ntorch.trace(input)\n'
import torch
input = torch.randn(3, 3)
output = torch.trace(input)
print('Input data: ', input)
print('Output data: ', output)