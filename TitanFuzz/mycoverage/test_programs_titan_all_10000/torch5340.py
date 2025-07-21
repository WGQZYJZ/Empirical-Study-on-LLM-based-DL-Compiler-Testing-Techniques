import torch
from torch import nn
from torch.autograd import Variable
input = torch.arange(1, 9, dtype=torch.float32).view(1, 1, 2, 4)
padding = (1, 2, 3, 4)
value = 0
output = torch.nn.ConstantPad2d(padding, value)(input)