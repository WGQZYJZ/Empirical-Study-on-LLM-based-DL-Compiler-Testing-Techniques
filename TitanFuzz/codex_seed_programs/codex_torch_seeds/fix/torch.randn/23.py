'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randn\ntorch.randn(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.randn(1, 2, 3, 4)
print(x)
'\ntorch.randn_like(input, dtype=None, layout=None, device=None, requires_grad=False)\n'
y = torch.randn_like(x)
print(y)
'\ntorch.rand(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
z = torch.rand(2, 3)
print(z)
'\ntorch.rand_like(input, dtype=None, layout=None, device=None, requires_grad=False)\n'
a = torch.rand_like(z)
print(a)