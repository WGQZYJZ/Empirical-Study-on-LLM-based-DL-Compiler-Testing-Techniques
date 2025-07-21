import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(3, 4, 5)
b = torch.swapaxes(a, 1, 2)