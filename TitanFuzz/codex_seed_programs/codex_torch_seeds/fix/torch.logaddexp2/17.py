'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logaddexp2\ntorch.logaddexp2(input, other, *, out=None)\n'
import torch
a = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)
c = torch.logaddexp2(a, b)
print(c)
c.backward()
print(a.grad, b.grad)