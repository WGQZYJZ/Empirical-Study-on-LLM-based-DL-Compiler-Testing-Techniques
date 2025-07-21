import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 4, 4, 4)
lrn = torch.nn.LocalResponseNorm(2)
output = lrn(input)