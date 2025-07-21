'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.no_grad\ntorch.no_grad()\n'
import torch
x = torch.randn(3, requires_grad=True)
y = (x * 2)
with torch.no_grad():
    y = (x * 2)
print(x.requires_grad)
print(y.requires_grad)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.no_grad\ntorch.set_grad_enabled\n'
import torch
x = torch.randn(3, requires_grad=True)
y = (x * 2)
with torch.set_grad_enabled(False):
    y = (x * 2)
print(x.requires_grad)
print(y.requires_grad)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.no_grad\ntorch.autograd.grad\n'