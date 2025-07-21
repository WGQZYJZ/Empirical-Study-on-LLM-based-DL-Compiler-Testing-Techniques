import torch
from torch import nn
from torch.autograd import Variable
a = torch.rand(3, 5)
b = torch.rand(3, 5)
c = torch.rand(3, 5)
out = torch.dstack((a, b, c))