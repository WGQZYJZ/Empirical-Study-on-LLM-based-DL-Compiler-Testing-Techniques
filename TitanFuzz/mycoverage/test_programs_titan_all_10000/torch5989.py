import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3)
y = torch.randn(2, 3)
d = torch.dist(x, y, p=2)