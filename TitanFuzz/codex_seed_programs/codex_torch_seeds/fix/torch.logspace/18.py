'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logspace\ntorch.logspace(start, end, steps, base=10.0, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.linspace(0.01, 10, steps=10)
print(x)
y = torch.logspace(start=0.1, end=1, steps=10)
print(y)