'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.geqrf\ntorch.geqrf(input, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(2, 3)
print('Input:')
print(input)
print('Task 3: Call the API torch.geqrf')
output = torch.geqrf(input)
print('Output:')
print(output)