import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
output = torch.renorm(input, 1, 0, 2)