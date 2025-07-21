import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(1, 3)
output = torch.arccosh(input)