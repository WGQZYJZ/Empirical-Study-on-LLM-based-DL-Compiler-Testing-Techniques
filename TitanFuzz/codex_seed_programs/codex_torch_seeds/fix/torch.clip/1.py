'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clip\ntorch.clip(input, min=None, max=None, *, out=None)\n'
import torch
x = torch.randn(10, 5)
print('x = ', x)
x_clipped = torch.clip(x, min=0.5, max=0.7)
print('x_clipped = ', x_clipped)
x_clipped_2 = torch.clamp(x, min=0.5, max=0.7)
print('x_clipped_2 = ', x_clipped_2)