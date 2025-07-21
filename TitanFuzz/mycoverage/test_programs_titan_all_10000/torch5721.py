import torch
from torch import nn
from torch.autograd import Variable
x1 = torch.randn(1000, 3)
x2 = torch.randn(1000, 3)
dist = torch.cdist(x1, x2)