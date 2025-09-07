import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(2, 3)
n = 5
out = torch.special.polygamma(n, input)