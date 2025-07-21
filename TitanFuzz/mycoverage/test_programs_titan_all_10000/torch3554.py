import torch
from torch import nn
from torch.autograd import Variable
input = torch.ones(1, 1, 3, 3)
padding_value = torch.nn.ConstantPad2d(padding=(1, 1, 1, 1), value=0)
output = padding_value(input)