import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 3)
y = torch.nn.Hardtanh(min_val=(- 1.0), max_val=1.0, inplace=False)(x)