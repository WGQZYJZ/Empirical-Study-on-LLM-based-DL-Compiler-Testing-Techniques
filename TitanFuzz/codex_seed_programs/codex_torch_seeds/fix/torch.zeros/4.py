'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.zeros\ntorch.zeros(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.rand(5, 3)
print(x)
y = torch.zeros(5, 3, dtype=torch.long)
print(y)
z = torch.tensor([5.5, 3])
print(z)
'\ntorch.randn_like(*tensors, dtype=None, layout=None, device=None, requires_grad=False)\n'
x = torch.rand(5, 3)
print(x)
y = torch.randn_like(x, dtype=torch.float)
print(y)
'\ntorch.randint(low, high, size, *, generator=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
x = torch.randint(3, 10, (3, 3))
print(x)