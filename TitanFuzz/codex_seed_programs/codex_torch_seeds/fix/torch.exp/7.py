'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp\ntorch.exp(input, *, out=None)\n'
import torch
x = torch.randn(1, requires_grad=True)
y = torch.exp(x)
print(y)
y.backward()
print(x.grad)