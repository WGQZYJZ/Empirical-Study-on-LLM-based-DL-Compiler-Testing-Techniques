import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(5, 5))
y = Variable(torch.randn(5, 5))
z = torch.igamma(x, y)