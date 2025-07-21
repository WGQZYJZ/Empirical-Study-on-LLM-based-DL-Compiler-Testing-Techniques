import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(10, 10)
output = torch.special.polygamma(1, input)