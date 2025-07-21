import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 2)
output = torch.nn.Hardtanh(min_val=(- 1.0), max_val=1.0, inplace=False)(input)