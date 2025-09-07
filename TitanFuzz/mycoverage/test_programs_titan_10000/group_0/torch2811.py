import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(5, 3)
x = torch.randn(5, 3)
x = torch.randint(5, 10, (5, 3))
x = torch.randperm(5)