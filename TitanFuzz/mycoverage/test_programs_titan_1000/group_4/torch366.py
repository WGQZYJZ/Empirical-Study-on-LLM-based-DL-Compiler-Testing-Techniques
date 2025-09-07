import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 4))
pool = torch.nn.AdaptiveMaxPool1d(1)
output = pool(input)