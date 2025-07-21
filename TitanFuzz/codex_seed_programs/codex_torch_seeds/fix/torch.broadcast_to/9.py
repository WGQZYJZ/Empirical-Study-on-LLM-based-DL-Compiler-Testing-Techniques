'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_to\ntorch.broadcast_to(input, shape)\n'
import torch
input = torch.rand(2, 3)
print('input = ', input)
shape = (4, 2, 3)
print('shape = ', shape)
output = torch.broadcast_to(input, shape)
print('output = ', output)