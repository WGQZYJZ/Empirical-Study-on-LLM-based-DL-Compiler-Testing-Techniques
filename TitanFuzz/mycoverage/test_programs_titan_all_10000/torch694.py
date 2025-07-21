import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(3, 4)
output = torch.cumprod(input, dim=1)