'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.movedim\ntorch.movedim(input, source, destination)\n'
import torch
input = torch.randn(1, 2, 3, 4)
print('input:', input)
print('input shape:', input.shape)
print('\nTask 2: Generate input data')
print('input:', input)
print('input shape:', input.shape)
print('\nTask 3: Call the API torch.movedim')
output = torch.movedim(input, 0, (- 1))
print('output:', output)
print('output shape:', output.shape)