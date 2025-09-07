import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(1, 3)
b = torch.randn(1, 3)
c = torch.greater(a, b)