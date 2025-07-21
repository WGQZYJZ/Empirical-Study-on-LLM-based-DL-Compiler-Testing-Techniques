import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
quantile_value = torch.quantile(input, 0.5)