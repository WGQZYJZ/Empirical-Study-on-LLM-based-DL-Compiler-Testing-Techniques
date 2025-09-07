import torch
from torch import nn
from torch.autograd import Variable

x = torch.full((2,), 10.0)
x = torch.randn(2, 3)
x = torch.full((2, 3), 10.0)