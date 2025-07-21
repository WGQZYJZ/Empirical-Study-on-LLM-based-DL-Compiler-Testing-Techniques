import torch
from torch import nn
from torch.autograd import Variable
dtype = torch.FloatTensor
(N, C, H, W) = (3, 4, 5, 6)
x = Variable(torch.randn(N, C, H, W).type(dtype), requires_grad=False)
padding = (1, 2, 3, 4)
y = torch.nn.ZeroPad2d(padding)(x)