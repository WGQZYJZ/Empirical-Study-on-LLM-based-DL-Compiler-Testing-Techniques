'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lerp\ntorch.lerp(input, end, weight, *, out=None)\n'
import torch
input = torch.randn(4, 4)
end = torch.randn(4, 4)
weight = torch.randn(4, 4)
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('\nTask 2: Generate input data')
print('Input data: ', input)
print('End data: ', end)
print('Weight data: ', weight)
print('\nTask 3: Call the API torch.lerp')
result = torch.lerp(input, end, weight)
print('Result: ', result)