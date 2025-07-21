import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4)
(mantissa, exponent) = torch.frexp(x)