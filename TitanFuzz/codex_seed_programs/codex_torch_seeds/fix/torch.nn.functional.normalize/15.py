'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.normalize\ntorch.nn.functional.normalize(input, p=2.0, dim=1, eps=1e-12, out=None)\n'
import torch
import torch.nn.functional as F
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(4, 5)
print('Input data:')
print(input)
print('Task 3: Call the API torch.nn.functional.normalize')
output = F.normalize(input, p=2.0, dim=1, eps=1e-12, out=None)
print('Output data:')
print(output)