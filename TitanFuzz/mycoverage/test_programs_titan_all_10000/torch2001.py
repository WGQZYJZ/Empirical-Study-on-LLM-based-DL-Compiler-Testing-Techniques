import torch
from torch import nn
from torch.autograd import Variable
a = torch.rand(3, 3)
b = torch.rand(3, 3)
c = torch.minimum(a, b)