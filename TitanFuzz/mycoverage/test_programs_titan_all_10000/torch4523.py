import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4)
y = torch.randn(4)
z = torch.atan2(x, y)