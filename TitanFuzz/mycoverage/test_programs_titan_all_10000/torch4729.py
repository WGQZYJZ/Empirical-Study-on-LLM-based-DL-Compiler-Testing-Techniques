import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, requires_grad=True)
y = torch.special.expit(x)
y.backward(torch.ones(3))