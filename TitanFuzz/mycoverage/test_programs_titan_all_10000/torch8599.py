import torch
from torch import nn
from torch.autograd import Variable
x = torch.linspace((- 10), 10, 10, requires_grad=True)
y = torch.special.expit(x)
y.backward(torch.ones(10))