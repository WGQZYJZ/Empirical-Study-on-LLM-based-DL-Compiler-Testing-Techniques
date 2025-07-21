'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arange\ntorch.arange(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.arange(0, 10, 0.1)
print(x)
'\nTask 4: Call the API torch.linspace\ntorch.linspace(start, end, steps=100, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
x = torch.linspace(0, 10, 10)
print(x)
'\nTask 5: Call the API torch.logspace\ntorch.logspace(start, end, steps=100, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
x = torch.logspace(0, 10, 10)
print(x)
'\nTask 6: Call the API torch.ones\ntorch.ones(size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
x = torch.ones(5)
print(x)