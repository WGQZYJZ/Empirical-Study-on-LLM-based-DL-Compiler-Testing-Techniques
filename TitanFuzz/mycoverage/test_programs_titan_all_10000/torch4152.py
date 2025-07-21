import torch
from torch import nn
from torch.autograd import Variable
data = torch.rand(5, 3)
(mantissa, exponent) = torch.frexp(data)