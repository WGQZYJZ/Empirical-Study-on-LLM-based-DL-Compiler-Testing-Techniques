import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(5, 5))
y = torch.nn.functional.softplus(x)