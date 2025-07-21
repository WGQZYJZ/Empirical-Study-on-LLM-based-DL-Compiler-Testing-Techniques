import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(10, dtype=torch.float)
output = torch.special.gammaln(input)