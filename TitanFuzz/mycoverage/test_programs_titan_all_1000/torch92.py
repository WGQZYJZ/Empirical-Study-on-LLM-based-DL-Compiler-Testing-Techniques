import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 5))
output = torch.nn.Softsign()(input)