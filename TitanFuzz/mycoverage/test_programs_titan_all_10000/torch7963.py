import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3, 3)
padding = (1, 1, 1, 1)
value = 0
pad = torch.nn.ConstantPad2d(padding, value)
output = pad(input)