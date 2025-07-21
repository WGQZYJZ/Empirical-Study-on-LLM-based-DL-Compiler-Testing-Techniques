import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(2, 3))
target = Variable(torch.randn(2, 3))
output = torch.nn.functional.kl_div(input, target)