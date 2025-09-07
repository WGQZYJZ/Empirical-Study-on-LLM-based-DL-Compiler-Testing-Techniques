import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4, 4)
y = torch.randn(4, 4)
z = torch.div(x, y)
z = torch.div(x, 10)