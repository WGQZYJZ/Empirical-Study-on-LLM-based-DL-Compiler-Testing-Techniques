import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 1, 3, 3, 3))
padding = (1, 1, 1, 1, 1, 1)
output = torch.nn.ReflectionPad3d(padding)(input_data)