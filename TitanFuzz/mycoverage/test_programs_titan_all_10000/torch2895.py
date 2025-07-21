import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(8, 6)
output = torch.hsplit(input, 3)