import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(1, 1, 5, 5))
relu = torch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)
y = relu(x)