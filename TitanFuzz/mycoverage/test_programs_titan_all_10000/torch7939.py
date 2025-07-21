import torch
from torch import nn
from torch.autograd import Variable
x1 = torch.rand(3, 10)
x2 = torch.rand(3, 10)
dist = torch.cdist(x1, x2)