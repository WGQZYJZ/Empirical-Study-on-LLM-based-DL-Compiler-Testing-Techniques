import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4)
output = torch.erfinv(x)