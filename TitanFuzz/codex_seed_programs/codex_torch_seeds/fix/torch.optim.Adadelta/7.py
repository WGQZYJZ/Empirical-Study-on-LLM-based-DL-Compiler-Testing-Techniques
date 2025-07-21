'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adadelta\ntorch.optim.Adadelta(params, lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.ones(2, 2), requires_grad=True)
optimizer = torch.optim.Adadelta(params=[x], lr=0.001, rho=0.9, eps=1e-06, weight_decay=0)
optimizer.zero_grad()
optimizer.step()
print(optimizer.param_groups)
print(optimizer.state)