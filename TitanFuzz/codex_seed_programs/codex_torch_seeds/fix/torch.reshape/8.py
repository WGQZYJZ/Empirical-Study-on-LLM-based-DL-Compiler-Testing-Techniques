'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reshape\ntorch.reshape(input, shape)\n'
import torch
input = torch.randn(2, 3, 4)
print('input = ', input)
output = torch.reshape(input, (3, 8))
print('output = ', output)