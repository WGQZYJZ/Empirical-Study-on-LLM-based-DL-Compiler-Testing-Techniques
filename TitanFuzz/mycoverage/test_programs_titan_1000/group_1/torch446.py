import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 10)
other = torch.randn(1, 10)
output = torch.nextafter(input, other)