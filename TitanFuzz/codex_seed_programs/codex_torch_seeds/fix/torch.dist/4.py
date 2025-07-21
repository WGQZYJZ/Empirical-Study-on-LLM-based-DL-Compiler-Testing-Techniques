'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dist\ntorch.dist(input, other, p=2)\n'
import torch
x = torch.randn(3, requires_grad=True)
y = torch.randn(3, requires_grad=True)
z = torch.dist(x, y, p=2)
print('z=', z)
z.backward()
print('x.grad=', x.grad)
print('y.grad=', y.grad)