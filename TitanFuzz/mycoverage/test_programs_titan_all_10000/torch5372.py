import torch
from torch import nn
from torch.autograd import Variable
input = torch.ones(1, 1, 3, 3)
pad = torch.nn.ReflectionPad2d(1)
output = pad(input)