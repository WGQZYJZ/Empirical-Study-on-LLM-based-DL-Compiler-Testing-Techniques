import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(1, dtype=torch.float64)
output = torch.special.erfinv(input)