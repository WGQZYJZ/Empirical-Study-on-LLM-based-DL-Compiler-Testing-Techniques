'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cummax\ntorch.cummax(input, dim, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('PyTorch version:', torch.__version__)
print('\nTask 2: Generate input data')
input = torch.randn(2, 3)
print('input:', input)
print('\nTask 3: Call the API torch.cummax')
print('torch.cummax(input, dim, *, out=None)')
print('input:', input)
print('dim:', 0)
print('torch.cummax(input, dim, *, out=None):', torch.cummax(input, 0))
print('dim:', 1)
print('torch.cummax(input, dim, *, out=None):', torch.cummax(input, 1))