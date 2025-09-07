import torch
from torch import nn
from torch.autograd import Variable
y = torch.randn(3, 4)
result = torch.cumulative_trapezoid(y)