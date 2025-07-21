import torch
from torch import nn
from torch.autograd import Variable
input = torch.arange(1, 10, dtype=torch.float).reshape(3, 3)
output = torch.renorm(input, p=1, dim=0, maxnorm=1)