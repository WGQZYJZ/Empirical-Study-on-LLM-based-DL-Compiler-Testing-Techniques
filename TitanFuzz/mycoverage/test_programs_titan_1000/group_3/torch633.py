import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 10)
output = torch.expm1(input)