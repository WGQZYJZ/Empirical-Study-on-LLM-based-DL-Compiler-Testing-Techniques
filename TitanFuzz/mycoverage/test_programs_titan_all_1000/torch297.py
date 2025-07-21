import torch
from torch import nn
from torch.autograd import Variable
a = torch.rand(3, 5)
b = torch.rand(3, 5)
c = torch.div(a, b)