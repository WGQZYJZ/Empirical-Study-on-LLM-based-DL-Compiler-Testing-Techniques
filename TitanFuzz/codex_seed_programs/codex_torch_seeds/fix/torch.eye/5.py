'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eye\ntorch.eye(n, m=None, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.randn(1, 3)
print(torch.eye(3))
print(torch.eye(3, 3))
print(torch.eye(3, 3, dtype=torch.int))
print(torch.eye(3, 4))
print(torch.eye(3, 4, dtype=torch.int))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linspace\ntorch.linspace(start, end, steps=100, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.randn(1, 3)
print(torch.linspace(2, 10, steps=5))
print(torch.linspace(2, 10, steps=5, dtype=torch.int))