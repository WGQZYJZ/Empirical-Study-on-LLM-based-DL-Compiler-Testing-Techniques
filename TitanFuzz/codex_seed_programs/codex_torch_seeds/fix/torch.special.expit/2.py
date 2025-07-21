'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.expit\ntorch.special.expit(input, *, out=None)\n'
import torch
x = torch.linspace((- 10), 10, 10, requires_grad=True)
print('Input data: ', x)
y = torch.special.expit(x)
print('Output data: ', y)
'\nTask 4: Compute the gradient\n'
y.backward(torch.ones(10))
print('Gradient: ', x.grad)