import torch
from torch import nn
from torch.autograd import Variable
y = torch.rand(3, 4)
torch.cumulative_trapezoid(y, dx=0.5)