import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(20, 20))
torch.nn.init.kaiming_uniform_(input)