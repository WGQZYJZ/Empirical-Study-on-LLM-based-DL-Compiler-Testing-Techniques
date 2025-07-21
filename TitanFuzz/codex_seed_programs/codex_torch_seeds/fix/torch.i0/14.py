'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.i0\ntorch.i0(input, *, out=None)\n'
import torch
x = torch.randn(1, requires_grad=True)
y = torch.i0(x)
y.backward()
print(x.grad)