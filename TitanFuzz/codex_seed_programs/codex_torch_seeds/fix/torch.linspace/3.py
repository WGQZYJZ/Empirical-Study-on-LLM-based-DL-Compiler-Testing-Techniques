'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linspace\ntorch.linspace(start, end, steps, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.linspace(start=0.0, end=1.0, steps=10)
print(x)
print(x.shape)
'\nTask 4: Call the API torch.randn\ntorch.randn(size, *, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
x = torch.randn(size=(3, 5))
print(x)
print(x.shape)
'\nTask 5: Call the API torch.randint\ntorch.randint(low, high, size, *, generator=None, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
x = torch.randint(low=0, high=10, size=(3, 5))
print(x)
print(x.shape)