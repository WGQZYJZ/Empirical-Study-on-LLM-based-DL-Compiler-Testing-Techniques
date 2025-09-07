import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(5)
output = torch.remainder(input, 2)