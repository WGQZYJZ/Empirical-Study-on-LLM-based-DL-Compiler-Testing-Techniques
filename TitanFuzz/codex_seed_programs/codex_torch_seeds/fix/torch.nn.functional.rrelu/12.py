'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.rrelu\ntorch.nn.functional.rrelu(input, lower=1./8, upper=1./3, training=False, inplace=False)\n'
import torch
x = torch.randn(1, 2, 3, requires_grad=True)
print(x)
y = torch.nn.functional.rrelu(x)
print(y)
y.sum().backward()
print(x.grad)