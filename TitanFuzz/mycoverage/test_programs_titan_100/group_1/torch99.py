import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 5, 5))
pool = torch.nn.AvgPool2d(2, 2)
output = pool(input)