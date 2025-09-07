import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 4))
output = torch.nn.functional.adaptive_avg_pool1d(input, 3)