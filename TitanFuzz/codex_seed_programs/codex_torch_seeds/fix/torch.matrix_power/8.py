'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_power\ntorch.matrix_power(input, n, *, out=None)\n'
import torch
input = torch.randn(1, 3, 3)
print('input = ', input)
print('\nTask 3: Call the API torch.matrix_power')
print('torch.matrix_power(input, n, *, out=None)')
print('n = 2')
output = torch.matrix_power(input, 2)
print('output = ', output)
print('\nTask 3: Call the API torch.matrix_power')
print('torch.matrix_power(input, n, *, out=None)')
print('n = 3')
output = torch.matrix_power(input, 3)
print('output = ', output)