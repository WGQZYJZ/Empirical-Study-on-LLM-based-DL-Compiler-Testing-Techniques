'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.div\ntorch.div(input, other, *, rounding_mode=None, out=None)\n'
import torch
x = torch.rand(3, 3)
y = torch.rand(3, 3)
print(x)
print(y)
z = torch.div(x, y)
print(z)