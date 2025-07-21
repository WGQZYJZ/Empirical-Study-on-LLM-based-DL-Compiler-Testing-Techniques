'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.rrelu\ntorch.nn.functional.rrelu(input, lower=1./8, upper=1./3, training=False, inplace=False)\n'
import torch
x = torch.linspace((- 1), 1, 10, requires_grad=True)
y = torch.nn.functional.rrelu(x, lower=0.1, upper=0.2)
print(y)
y.backward(torch.ones_like(x))
print(x.grad)