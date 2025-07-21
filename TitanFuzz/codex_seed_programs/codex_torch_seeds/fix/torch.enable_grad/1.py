'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.enable_grad\ntorch.enable_grad()\n'
import torch
import numpy as np
x = torch.tensor([[1.0, (- 1.0)], [1.0, (- 1.0)]], requires_grad=True)
torch.enable_grad()
y = (x ** 2)
z = ((2 * y) + 3)
z.backward(torch.ones_like(x))
print(x.grad)
print((x / 2))
print((x ** 2).requires_grad)
with torch.no_grad():
    print((x ** 2).requires_grad)
print(x.requires_grad)
print((x ** 2).requires_grad)
y = x.detach()
print(x.requires_grad)
print(y.requires_grad)