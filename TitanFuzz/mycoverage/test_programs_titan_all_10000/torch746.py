import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(5, 5)
output = torch.frac(input)