'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.remainder\ntorch.remainder(input, other, *, out=None)\n'
import torch
import torch
x = torch.randn(100)
y = torch.randn(100)
z = torch.remainder(x, y)
print(z)