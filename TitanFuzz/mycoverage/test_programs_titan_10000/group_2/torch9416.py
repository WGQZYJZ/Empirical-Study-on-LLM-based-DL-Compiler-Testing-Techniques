import torch
from torch import nn
from torch.autograd import Variable

input = torch.rand(3, 3)
torch.special.gammaln(input)
input = torch.rand(3, 3)
torch.special.digamma(input)