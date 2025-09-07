import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(3, 3, 3)
padding = (1, 1, 1, 1)
output = torch.nn.ZeroPad2d(padding)(input)