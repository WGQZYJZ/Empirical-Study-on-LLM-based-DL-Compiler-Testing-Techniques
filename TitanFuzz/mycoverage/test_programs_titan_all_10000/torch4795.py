import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(10, 10)
var = torch.var(input, dim=0)