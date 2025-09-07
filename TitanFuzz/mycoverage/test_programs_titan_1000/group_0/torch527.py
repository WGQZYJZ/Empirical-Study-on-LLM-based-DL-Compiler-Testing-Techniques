import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(10, 10)
y = torch.msort(x)