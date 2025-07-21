'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.abs\ntorch.abs(input, *, out=None)\n'
import torch
x = torch.randn(1, 2, 3, requires_grad=True)
y = torch.abs(x)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acos\ntorch.acos(input, *, out=None)\n'
import torch
x = torch.randn(1, 2, 3, requires_grad=True)
y = torch.acos(x)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.add\ntorch.add(input, other, *, alpha=1, out=None)\n'
import torch
x = torch.randn(1, 2, 3, requires_grad=True)
y = torch.add(x, x)
print(y)