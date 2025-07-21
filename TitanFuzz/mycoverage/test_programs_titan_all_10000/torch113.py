import torch
from torch import nn
from torch.autograd import Variable
dtype = torch.FloatTensor
(N, C, H, W) = (2, 3, 4, 4)
a = torch.randn(N, C, H, W).type(dtype)
a = Variable(a, requires_grad=False)
pool = torch.nn.LPPool2d(2, 3, stride=2, ceil_mode=False)
h = pool(a)