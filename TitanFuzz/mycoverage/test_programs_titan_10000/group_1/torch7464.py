import torch
from torch import nn
from torch.autograd import Variable

a = torch.randn(2, 3)
b = torch.tile(a, (2, 2))