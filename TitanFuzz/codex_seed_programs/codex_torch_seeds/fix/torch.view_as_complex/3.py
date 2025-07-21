'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.view_as_complex\ntorch.view_as_complex(input)\n'
import torch
print('\nTask 1: import PyTorch')
print('\nTask 2: Generate input data')
input = torch.rand(4, 2)
print('input: {}'.format(input))
print('\nTask 3: Call the API torch.view_as_complex')
output = torch.view_as_complex(input)
print('output: {}'.format(output))