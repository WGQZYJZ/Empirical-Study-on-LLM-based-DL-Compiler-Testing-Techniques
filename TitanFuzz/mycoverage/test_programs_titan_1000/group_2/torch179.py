import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 3)
output = torch.cumprod(input, dim=0)
output = torch.cumprod(input, dim=1)