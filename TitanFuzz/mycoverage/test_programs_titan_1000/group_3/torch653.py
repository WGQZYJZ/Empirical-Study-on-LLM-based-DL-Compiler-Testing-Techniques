import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 4)
other = torch.randn(3, 4)
output = torch.special.gammainc(input_data, other)