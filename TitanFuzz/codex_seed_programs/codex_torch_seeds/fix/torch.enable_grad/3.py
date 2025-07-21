'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.enable_grad\ntorch.enable_grad()\n'
import torch
import torch.nn as nn
x = torch.tensor([2.0, 3.0], requires_grad=True)
with torch.enable_grad():
    y = (x ** 2)
    z = y.mean()
z.backward()
print(x.grad)
print((x / 2))