import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
A = torch.randn(3, 3)
output = torch.lstsq(input, A)