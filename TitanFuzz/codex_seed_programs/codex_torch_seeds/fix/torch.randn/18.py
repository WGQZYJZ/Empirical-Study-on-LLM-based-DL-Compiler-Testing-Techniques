'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randn\ntorch.randn(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
a = torch.randn(5, 3)
print(a)
b = torch.randn(5, 3)
print(b)
c = torch.randn(5, 3)
print(c)
d = torch.add(a, b)
print(d)
e = torch.empty(5, 3)
torch.add(a, b, out=e)
print(e)
b.add_(a)
print(b)
print(a[:, 1])
a = torch.randn(4, 4)
print(a)
b