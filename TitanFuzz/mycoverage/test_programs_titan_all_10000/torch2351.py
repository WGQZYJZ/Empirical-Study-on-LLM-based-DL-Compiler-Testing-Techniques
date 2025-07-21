import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 4)
y = torch.randn(3, 4)
z = torch.randn(3, 4)
x_cat = torch.cat((x, y, z), dim=0)