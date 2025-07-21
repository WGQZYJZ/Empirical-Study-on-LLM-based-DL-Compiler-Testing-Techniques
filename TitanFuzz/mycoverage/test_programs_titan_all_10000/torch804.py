import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(10)
bins = 3
histogram = torch.histogram(input, bins)