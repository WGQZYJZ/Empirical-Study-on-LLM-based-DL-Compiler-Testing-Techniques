'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logit\ntorch.logit(input, eps=None, *, out=None)\n'
import torch
x = torch.randn(3, requires_grad=True)
print(x)
y = torch.logit(x)
print(y)
y.backward(torch.tensor([1, 1, 1]))
print(x.grad)
y = torch.logit(x, eps=1e-06)
print(y)
y.backward(torch.tensor([1, 1, 1]))
print(x.grad)