import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, dtype=torch.float)
result = torch.special.i1(input)