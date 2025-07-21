'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adadelta\ntorch.optim.Adadelta(params, lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)\n'
import torch
import numpy as np
import torch
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
adadelta = torch.optim.Adadelta(params=[x, y], lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)
print('x =', x)
print('y =', y)
print('lr =', adadelta.param_groups[0]['lr'])
print('rho =', adadelta.param_groups[0]['rho'])
print('eps =', adadelta.param_groups[0]['eps'])