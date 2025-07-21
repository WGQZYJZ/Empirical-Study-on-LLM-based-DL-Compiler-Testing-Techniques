'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rand_like\ntorch.rand_like(input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
x = torch.rand(4, 4)
print('Input data: ', x)
y = torch.rand_like(x)
print('Output data: ', y)