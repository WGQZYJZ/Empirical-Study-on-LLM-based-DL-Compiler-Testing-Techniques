import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(4)
(b, c) = torch.frexp(a)