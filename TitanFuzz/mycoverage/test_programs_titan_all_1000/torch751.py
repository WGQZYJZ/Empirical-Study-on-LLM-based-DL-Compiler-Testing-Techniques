import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(1, 5)
y = torch.arange(1, 5)
out = torch.cumulative_trapezoid(y, x)