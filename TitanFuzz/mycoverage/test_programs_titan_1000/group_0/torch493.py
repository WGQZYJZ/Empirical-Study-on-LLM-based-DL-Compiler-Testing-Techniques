import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 3, 3, 3))
reflectionPad2d = torch.nn.ReflectionPad2d(padding=1)
output = reflectionPad2d(input)