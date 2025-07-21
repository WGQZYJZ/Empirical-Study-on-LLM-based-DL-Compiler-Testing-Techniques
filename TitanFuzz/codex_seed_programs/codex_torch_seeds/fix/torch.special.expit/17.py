'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.expit\ntorch.special.expit(input, *, out=None)\n'
import torch
x = torch.randn(3, requires_grad=True)
print('x:', x)
y = torch.special.expit(x)
print('y:', y)
y.backward(torch.ones(3))
print('x.grad:', x.grad)