import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 10))
output = torch.nn.functional.adaptive_max_pool1d(input, 3)