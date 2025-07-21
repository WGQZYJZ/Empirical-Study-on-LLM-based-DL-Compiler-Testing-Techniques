'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adadelta\ntorch.optim.Adadelta(params, lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
x = torch.randn(2, 3, requires_grad=True)
print('x = torch.randn(2, 3, requires_grad=True)')
print('x = ', x)
print('Task 3: Call the API torch.optim.Adadelta')
optimizer = torch.optim.Adadelta(params=[x], lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)
print('optimizer = torch.optim.Adadelta(params=[x], lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)')
print('optimizer = ', optimizer)