import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 5)
padding = (2, 3)
value = 0
output = torch.nn.ConstantPad1d(padding, value)(input)