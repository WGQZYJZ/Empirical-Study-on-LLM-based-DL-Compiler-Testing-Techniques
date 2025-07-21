import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 2, 3, 3))
shrink = torch.nn.Hardshrink(lambd=0.5)
output = shrink(input_data)