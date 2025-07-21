'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ldexp\ntorch.ldexp(input, other, *, out=None)\n'
import torch
x = torch.randn(4)
y = torch.randn(4)
z = torch.ldexp(x, y)
print(z)