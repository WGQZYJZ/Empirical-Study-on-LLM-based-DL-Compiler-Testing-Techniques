'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less\ntorch.less(input, other, *, out=None)\n'
import torch
x = torch.randn(3, requires_grad=True)
y = torch.randn(3, requires_grad=True)
z = torch.less(x, y)
print(z)
x = torch.randn(3, requires_grad=True)
y = torch.randn(3, requires_grad=True)
z = torch.less_equal(x, y)
print(z)
x = torch.randn(3, requires_grad=True)
y = torch.randn(3, requires_grad=True)
z = torch.greater(x, y)
print(z)