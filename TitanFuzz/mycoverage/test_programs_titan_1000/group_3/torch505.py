import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 4, 5)
y = torch.randn(3, 4, 5)
torch.cross(x, y)