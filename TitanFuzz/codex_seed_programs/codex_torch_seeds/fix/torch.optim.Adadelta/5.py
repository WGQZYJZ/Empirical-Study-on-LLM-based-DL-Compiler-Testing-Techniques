'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adadelta\ntorch.optim.Adadelta(params, lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)\n'
import torch
import torch.nn as nn
x = torch.tensor(data=[2.0, 3.0], requires_grad=True)
y = torch.tensor(data=[4.0, 6.0], requires_grad=True)
optimizer = torch.optim.Adadelta(params=[x, y], lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)
print('Default hyper-parameters:\n', optimizer.defaults)
print('Actual hyper-parameters:\n', optimizer.state)
print('Parameter group:', optimizer.param_groups)
print('Current value of x:', x)
print('Current value of y:', y)