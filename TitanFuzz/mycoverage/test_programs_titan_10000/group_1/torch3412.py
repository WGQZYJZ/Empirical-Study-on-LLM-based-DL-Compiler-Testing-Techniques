import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(2, 3)
y = torch.randn(2, 5)
z = torch.hstack((x, y))