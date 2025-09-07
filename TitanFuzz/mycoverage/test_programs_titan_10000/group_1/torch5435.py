import torch
from torch import nn
from torch.autograd import Variable

input_data = Variable(torch.randn(1, 3, 3, 3))
hardswish = torch.nn.Hardswish()
output = hardswish(input_data)