import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 2, 3, dtype=torch.float)
out = torch.digamma(input)