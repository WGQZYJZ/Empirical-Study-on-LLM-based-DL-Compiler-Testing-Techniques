'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.no_grad\ntorch.no_grad()\n'
import torch
x = torch.randn(3, requires_grad=True)
print('x = ', x)
with torch.no_grad():
    y = (x * 2)
    print('y = ', y)
print('y.requires_grad = ', y.requires_grad)
print('y.grad_fn = ', y.grad_fn)
print('x.requires_grad = ', x.requires_grad)
print('x.grad_fn = ', x.grad_fn)
z = y.detach()
print('z = ', z)
print('z.requires_grad = ', z.requires_grad)
print('z.grad_fn = ', z.grad_fn)