import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 3, 3))
input = Variable(torch.randn(1, 1, 3, 3))
torch.nn.init.kaiming_normal_(input)