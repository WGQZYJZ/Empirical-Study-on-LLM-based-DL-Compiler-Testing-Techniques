import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(2, 3)
y = torch.special.exp2(x)