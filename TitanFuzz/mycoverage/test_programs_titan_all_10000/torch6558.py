import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3, requires_grad=True)
optimizer = torch.optim.Adadelta(params=[x], lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)