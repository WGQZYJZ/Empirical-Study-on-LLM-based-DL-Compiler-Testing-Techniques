'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.no_grad\ntorch.no_grad()\n'
import torch
x = torch.rand(5, 3)
y = torch.rand(5, 3)
with torch.no_grad():
    z = (x + y)
    print(z)
print(x.requires_grad)
print((x + y).requires_grad)
print(x.is_leaf, y.is_leaf, (x + y).is_leaf)
print(x.grad_fn)
print(y.grad_fn)
print((x + y).grad_fn)
print(x.requires_grad)
print(y.requires_grad)
print((x + y).requires_grad)