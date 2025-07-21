import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(10, 3)
torch.cov(input)