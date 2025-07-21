'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.digamma\ntorch.special.digamma(input, *, out=None)\n'
import torch
x = torch.randn(1, 1, requires_grad=True)
y = torch.special.digamma(x)
y.backward()
print(x)
print(y)
print(x.grad)