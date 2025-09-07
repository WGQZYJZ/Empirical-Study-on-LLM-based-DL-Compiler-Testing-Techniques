import torch
from torch import nn
from torch.autograd import Variable

a = torch.rand(3, 2)
b = torch.rand(3, 2)
c = torch.greater_equal(a, b)