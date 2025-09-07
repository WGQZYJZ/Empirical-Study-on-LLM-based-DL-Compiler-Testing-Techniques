import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(1, 1, 10, 10)
conv = torch.nn.LazyConv2d(1, 1, 3, padding=1)
y = conv(x)