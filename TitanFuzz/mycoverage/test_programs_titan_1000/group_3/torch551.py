import torch
from torch import nn
from torch.autograd import Variable
a = torch.rand(100, 100)
b = torch.rand(100, 100)
c = torch.isclose(a, b)