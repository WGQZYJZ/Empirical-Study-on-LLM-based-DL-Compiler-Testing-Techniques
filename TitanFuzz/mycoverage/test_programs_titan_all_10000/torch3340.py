import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 3)
mean_value = torch.mean(input)