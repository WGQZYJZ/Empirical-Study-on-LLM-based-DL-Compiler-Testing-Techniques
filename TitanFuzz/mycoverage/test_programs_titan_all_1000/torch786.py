import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(1, 3, 224, 224))
hardswish = torch.nn.Hardswish()
output = hardswish(x)