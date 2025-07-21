'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.zeros_like\ntorch.zeros_like(input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
x = torch.arange(4, dtype=torch.float32)
print('Input data: {}'.format(x))
y = torch.zeros_like(x)
print('Output data: {}'.format(y))