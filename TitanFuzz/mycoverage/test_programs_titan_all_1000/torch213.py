import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1)
output = torch.arctan(input)