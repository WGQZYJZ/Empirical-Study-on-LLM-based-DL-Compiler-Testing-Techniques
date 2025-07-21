import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3)
output = torch.special.polygamma(3, input)