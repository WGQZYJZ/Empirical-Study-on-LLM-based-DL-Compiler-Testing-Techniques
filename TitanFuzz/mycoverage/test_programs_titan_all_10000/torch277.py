import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(1, dtype=torch.double)
output = torch.lgamma(input)