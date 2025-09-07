import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(2, 3)
b = torch.masked_select(a, (a > 0))