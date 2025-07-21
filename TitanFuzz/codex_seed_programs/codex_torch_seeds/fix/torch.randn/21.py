'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randn\ntorch.randn(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.randn(2, 3)
print(x)
y = torch.rand(2, 3)
print(y)
z = torch.rand_like(x)
print(z)
a = torch.randint(2, 10, (2, 3))
print(a)