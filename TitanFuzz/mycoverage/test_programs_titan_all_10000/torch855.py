import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
output = torch.lgamma(input)
input = torch.randn(4, 4)
output = torch.log(input)
input = torch.randn(4, 4)