import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
index_min = torch.argmin(input, dim=1)