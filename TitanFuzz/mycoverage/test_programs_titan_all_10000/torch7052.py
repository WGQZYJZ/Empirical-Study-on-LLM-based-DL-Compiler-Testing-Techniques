import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(5, requires_grad=True)
y = torch.logit(x)
y.backward(torch.ones(5))