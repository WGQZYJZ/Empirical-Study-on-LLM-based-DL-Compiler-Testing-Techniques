'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.conj_physical\ntorch.conj_physical(input, *, out=None)\n'
import torch
a = torch.randn(3, 3)
print(a)
print(torch.conj_physical(a))
b = torch.randn(3, 3)
print(b)
print(torch.conj_physical(a, out=b))