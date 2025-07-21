import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 3)
output = torch.median(input, dim=(- 1), keepdim=False)