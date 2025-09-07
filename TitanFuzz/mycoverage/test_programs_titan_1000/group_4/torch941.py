import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 6, 6))
output = torch.nn.functional.adaptive_max_pool2d(input, (2, 2))