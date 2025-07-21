'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.ndtri\ntorch.special.ndtri(input, *, out=None)\n'
import torch
import torch
x = torch.randn(5, 5)
y = torch.special.ndtri(x)
print(y)