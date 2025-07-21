'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.ndtr\ntorch.special.ndtr(input, *, out=None)\n'
import torch
x = torch.randn(1, 1, requires_grad=True)
out = torch.special.ndtr(x)
print('x = ', x)
print('out = ', out)