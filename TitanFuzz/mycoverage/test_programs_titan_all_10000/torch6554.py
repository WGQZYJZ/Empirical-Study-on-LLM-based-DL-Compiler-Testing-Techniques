import torch
from torch import nn
from torch.autograd import Variable
a = torch.rand(2, 3)
b = torch.rand(2, 3)
c = torch.subtract(a, b)