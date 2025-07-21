'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full_like\ntorch.full_like(input, fill_value, *, dtype=None, layout=torch.strided, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
x = torch.randn(3, 3)
print(x)
y = torch.full_like(x, fill_value=4)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linspace\ntorch.linspace(start, end, steps=100, *, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.randn(3, 3)
print(x)
y = torch.linspace(start=0, end=1, steps=5)
print(y)