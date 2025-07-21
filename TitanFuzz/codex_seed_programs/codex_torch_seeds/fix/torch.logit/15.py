'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logit\ntorch.logit(input, eps=None, *, out=None)\n'
import torch
x = torch.rand(3, requires_grad=True)
print('x:', x)
y = torch.logit(x)
print('y:', y)
y.backward(torch.tensor([1.0, 1.0, 1.0]))
print('x.grad:', x.grad)