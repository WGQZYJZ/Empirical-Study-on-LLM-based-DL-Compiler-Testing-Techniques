import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4)
output = torch.unbind(input, dim=0)