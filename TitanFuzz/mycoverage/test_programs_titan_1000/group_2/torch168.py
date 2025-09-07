import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(20, 16, 50))
output = torch.nn.functional.lp_pool1d(input, 1, 2, stride=2)
output = torch.nn.functional.lp_pool1d(input, 2, 2, stride=2)