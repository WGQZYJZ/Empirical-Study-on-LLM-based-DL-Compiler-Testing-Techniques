import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(5, 5)
shrinked = torch.nn.functional.hardshrink(x)