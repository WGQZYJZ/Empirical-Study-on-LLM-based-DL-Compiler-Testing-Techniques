import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(100, 3)
cov = torch.cov(x)