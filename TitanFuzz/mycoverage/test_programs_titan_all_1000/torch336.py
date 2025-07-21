import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(1, 1, 3, 3)
output = torch.special.i0(input)