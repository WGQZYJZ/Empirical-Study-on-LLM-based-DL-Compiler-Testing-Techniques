'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rand_like\ntorch.rand_like(input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
input = torch.empty(5, 3)
print('Input data: ')
print(input)
output = torch.rand_like(input)
print('Output data: ')
print(output)