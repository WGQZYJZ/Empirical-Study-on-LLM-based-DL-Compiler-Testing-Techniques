'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.divide\ntorch.divide(input, other, *, rounding_mode=None, out=None)\n'
import torch
x = torch.rand(2, 3)
y = torch.rand(2, 3)
z = torch.divide(x, y)
print(z)