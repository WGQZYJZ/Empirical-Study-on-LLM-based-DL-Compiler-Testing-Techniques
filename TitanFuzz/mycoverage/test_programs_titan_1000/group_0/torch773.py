import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(2, 2, dtype=torch.float)
output = torch.special.digamma(input)