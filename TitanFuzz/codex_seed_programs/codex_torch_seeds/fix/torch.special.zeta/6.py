'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.zeta\ntorch.special.zeta(input, other, *, out=None)\n'
import torch
import torch.special
a = torch.randn(1, 3)
b = torch.randn(1, 3)
print(a)
print(b)
print(torch.special.zeta(a, b))