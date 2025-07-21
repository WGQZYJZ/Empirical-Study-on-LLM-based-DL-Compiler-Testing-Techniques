import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 2)
other = torch.randn(3, 2)
output = torch.sub(input, other)