import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 2)
output = torch.msort(input)