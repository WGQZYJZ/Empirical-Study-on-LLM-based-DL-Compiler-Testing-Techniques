import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(4, 3)
y = torch.rand(4, 3)
z = torch.hstack((x, y))