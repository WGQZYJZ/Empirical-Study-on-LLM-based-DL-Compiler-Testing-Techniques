import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(4, 4), requires_grad=True)
y = Variable(torch.randn(4, 4), requires_grad=True)
z = torch.special.xlogy(x, y)
z.backward(torch.ones(4, 4))