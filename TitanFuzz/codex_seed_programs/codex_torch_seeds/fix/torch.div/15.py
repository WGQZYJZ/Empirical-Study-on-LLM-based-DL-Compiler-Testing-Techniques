'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.div\ntorch.div(input, other, *, rounding_mode=None, out=None)\n'
import torch
x = torch.randn(4, 4)
y = torch.randn(4, 4)
z = torch.div(x, y)
print(x)
print(y)
print(z)