'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.no_grad\ntorch.no_grad()\n'
import torch
x = torch.rand(5, 3)
y = torch.rand(5, 3)
with torch.no_grad():
    z = (x + y)
    print(z)
x = torch.rand(5, 3, requires_grad=True)
y = torch.rand(5, 3, requires_grad=True)
z = (x + y)
print(z)
x = torch.rand(5, 3, requires_grad=True)
y = torch.rand(5, 3, requires_grad=True)
z = (x + y)
print(z.requires_grad)
x = torch.rand(5, 3, requires_grad=True)
y = torch.rand(5, 3, requires_grad=True)
z = (x + y)