import torch
from torch import nn
from torch.autograd import Variable
n = 3
input = torch.randn(4, 4)
output = torch.polygamma(n, input)