import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 3)
y = torch.rand(3, 3)
z = torch.hstack((x, y))
z = torch.cat((x, y), 1)