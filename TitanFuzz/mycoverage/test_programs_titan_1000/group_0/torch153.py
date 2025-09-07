import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(4, 4)
b = torch.reshape(a, (8, 2))