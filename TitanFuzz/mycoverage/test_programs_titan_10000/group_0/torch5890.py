import torch
from torch import nn
from torch.autograd import Variable

x = Variable(torch.randn(2, 3), requires_grad=True)
y = torch.nn.Threshold(0.5, 0)(x)