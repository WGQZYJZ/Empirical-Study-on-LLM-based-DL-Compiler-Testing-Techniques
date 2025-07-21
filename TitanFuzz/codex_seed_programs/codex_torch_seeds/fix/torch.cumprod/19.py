'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumprod\ntorch.cumprod(input, dim, *, dtype=None, out=None)\n'
import torch
import torch
x = torch.rand(3, 4)
print(x)
y = torch.cumprod(x, dim=1)
print(y)