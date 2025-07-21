'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.no_grad\ntorch.no_grad()\n'
import torch
x = torch.ones(2, 2, requires_grad=True)
print(x)
with torch.no_grad():
    y = (x + 2)
    print(y)
print(y.grad_fn)
print(y.requires_grad)
print(x.requires_grad)
print(x.grad_fn)
print(y.grad_fn)