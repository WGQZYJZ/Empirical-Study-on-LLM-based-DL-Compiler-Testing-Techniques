import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 5, 7, dtype=torch.float)
other = torch.randn(1, 3, 5, 7, dtype=torch.float)
output = torch.special.zeta(input, other)