'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mv\ntorch.mv(input, vec, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(2, 3)
print('input = ', input)
vec = torch.randn(3)
print('vec = ', vec)
print('Task 3: Call the API torch.mv')
output = torch.mv(input, vec)
print('output = ', output)
output = torch.mv(input, vec, out=torch.zeros(2))
print('output = ', output)