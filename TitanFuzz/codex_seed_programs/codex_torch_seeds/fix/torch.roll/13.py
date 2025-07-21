'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.roll\ntorch.roll(input, shifts, dims=None)\n'
import torch
print('\nTask 1: import PyTorch')
print('\nTask 2: Generate input data')
input = torch.randn(3, 4)
print('\ninput = ', input)
print('\nTask 3: Call the API torch.roll')
shifts = 1
dims = 0
output = torch.roll(input, shifts, dims)
print('\noutput = ', output)