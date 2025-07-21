import torch
from torch import nn
from torch.autograd import Variable
a = torch.arange(1, 6)
b = torch.arange(2, 7)
c = torch.subtract(a, b)