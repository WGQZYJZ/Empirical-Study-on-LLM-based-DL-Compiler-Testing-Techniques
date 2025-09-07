import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 2, 3)
y = torch.special.log1p(x)