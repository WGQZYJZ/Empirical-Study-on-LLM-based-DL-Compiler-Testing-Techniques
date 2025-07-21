import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(1000)
histogram = torch.histogram(input, bins=10, range=(0, 1))