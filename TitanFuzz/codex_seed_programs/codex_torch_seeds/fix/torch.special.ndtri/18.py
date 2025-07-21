'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.ndtri\ntorch.special.ndtri(input, *, out=None)\n'
import torch
x = torch.rand(2, 3)
print(x)
y = torch.special.ndtri(x)
print(y)