'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linspace\ntorch.linspace(start, end, steps, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.linspace(start=0, end=10, steps=5)
print(x)
y = torch.linspace(start=(- 10), end=10, steps=5)
print(y)
z = torch.linspace(start=0, end=1, steps=5)
print(z)
a = torch.linspace(start=0, end=1, steps=5, dtype=torch.int32)
print(a)
b = torch.linspace(start=0, end=1, steps=5, dtype=torch.int32, layout=torch.strided)
print(b)
c = torch.linspace(start=0, end=1, steps=5, dtype=torch.int32, layout=torch.strided, device='cpu')
print(c)