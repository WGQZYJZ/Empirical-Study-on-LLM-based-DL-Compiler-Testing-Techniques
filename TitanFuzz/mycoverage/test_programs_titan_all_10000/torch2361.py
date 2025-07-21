import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 5))
pool = torch.nn.AvgPool1d(kernel_size=2, stride=2, padding=0)
output = pool(input)