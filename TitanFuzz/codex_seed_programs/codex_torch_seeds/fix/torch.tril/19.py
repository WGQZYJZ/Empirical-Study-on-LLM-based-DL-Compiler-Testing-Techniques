'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tril\ntorch.tril(input, diagonal=0, *, out=None)\n'
import torch
x = torch.rand(3, 3)
print('Input data: \n', x)
print('\nAPI: torch.tril(input, diagonal=0, *, out=None)')
print('Output: \n', torch.tril(x))
print('\nAPI: torch.tril(input, diagonal=1, *, out=None)')
print('Output: \n', torch.tril(x, 1))
print('\nAPI: torch.tril(input, diagonal=-1, *, out=None)')
print('Output: \n', torch.tril(x, (- 1)))