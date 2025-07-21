'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_to\ntorch.broadcast_to(input, shape)\n'
import torch
input = torch.randn(2, 3)
print('input:')
print(input)
print('input.shape:')
print(input.shape)
output = torch.broadcast_to(input, (4, 2, 3))
print('output:')
print(output)
print('output.shape:')
print(output.shape)