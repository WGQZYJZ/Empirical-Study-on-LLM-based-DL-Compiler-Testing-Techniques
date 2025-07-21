import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1000)
hist = torch.histogram(x, bins=100)