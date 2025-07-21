'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.no_grad\ntorch.no_grad()\n'
import torch
x = torch.randn(1, requires_grad=True)
w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)
with torch.no_grad():
    y = ((w * x) + b)
print(x)
print(w)
print(b)
print(y)