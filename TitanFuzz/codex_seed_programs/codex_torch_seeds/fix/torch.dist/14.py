'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dist\ntorch.dist(input, other, p=2)\n'
import torch
print('Task 1: import PyTorch')
print('PyTorch version: {}'.format(torch.__version__))
print('CUDA available: {}'.format(torch.cuda.is_available()))
print('\nTask 2: Generate input data')
x = torch.rand(3, 4)
y = torch.rand(3, 4)
print('x: {}'.format(x))
print('y: {}'.format(y))
print('\nTask 3: Call the API torch.dist')
print('torch.dist(x, y, p=2): {}'.format(torch.dist(x, y, p=2)))