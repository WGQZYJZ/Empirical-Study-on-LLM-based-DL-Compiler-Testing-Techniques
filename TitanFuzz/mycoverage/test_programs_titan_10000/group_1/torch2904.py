import torch
from torch import nn
from torch.autograd import Variable

input_data = Variable(torch.randn(1, 10))
output = torch.special.i0(input_data)