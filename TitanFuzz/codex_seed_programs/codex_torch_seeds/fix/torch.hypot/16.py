'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hypot\ntorch.hypot(input, other, *, out=None)\n'
import torch
x = torch.randn(3, 4)
y = torch.randn(3, 4)
z = torch.hypot(x, y)
print(z)