import torch
from torch import nn
from torch.autograd import Variable
dtype = torch.FloatTensor
(N, C, H, W) = (1, 2, 3, 3)
x = Variable(torch.randn(N, C, H, W).type(dtype), requires_grad=False)
max_pool = torch.nn.MaxPool2d(2, stride=2)
y = max_pool(x)