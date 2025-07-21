'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clone\ntorch.clone(input, *, memory_format=torch.preserve_format)\n'
import torch
x = torch.ones(2, 2, requires_grad=True)
print('x:', x)
y = (x + 2)
print('y:', y)
z = ((y * y) * 3)
out = z.mean()
print('z:', z)
print('out:', out)
out.backward()
print('x.grad:', x.grad)
x_clone = torch.clone(x, memory_format=torch.preserve_format)
print('x_clone:', x_clone)