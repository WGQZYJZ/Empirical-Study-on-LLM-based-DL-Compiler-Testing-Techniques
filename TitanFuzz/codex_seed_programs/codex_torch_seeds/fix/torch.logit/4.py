'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logit\ntorch.logit(input, eps=None, *, out=None)\n'
import torch
x = torch.randn(5, requires_grad=True)
y = torch.logit(x)
print(y)
y.backward(torch.ones(5))
print(x.grad)