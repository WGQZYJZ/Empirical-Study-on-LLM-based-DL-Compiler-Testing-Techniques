'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randint_like\ntorch.randint_like(input, low=0, high, *, dtype=None, layout=torch.strided, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randint(10, (3, 3), dtype=torch.float)
print('input:', input)
print('Task 3: Call the API torch.randint_like')
output = torch.randint_like(input, low=0, high=10)
print('output:', output)