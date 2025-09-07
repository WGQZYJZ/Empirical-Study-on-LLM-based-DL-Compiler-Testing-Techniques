import torch
from torch import nn
from torch.autograd import Variable
y = torch.rand(3, 5)
torch.cumulative_trapezoid(y)
torch.cumulative_trapezoid(y, dim=0)
torch.cumulative_trapezoid(y, dim=1)
torch.cumulative_trapezoid(y, dim=(- 1))
torch.cumulative_trapezoid(y, dim=(- 2))