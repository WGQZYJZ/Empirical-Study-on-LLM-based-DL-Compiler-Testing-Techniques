import torch
from torch import nn
from torch.autograd import Variable

input = Variable(torch.randn(1, 1))
output = torch.nn.functional.elu(input)