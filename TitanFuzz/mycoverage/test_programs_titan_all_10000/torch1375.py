import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(5)
x = Variable(x, requires_grad=True)
y = torch.nn.Softplus()(x)
y.backward(torch.ones(5))
x = torch.randn(5)
x = Variable(x, requires_grad=True)
y = torch.nn.Tanh()(x)