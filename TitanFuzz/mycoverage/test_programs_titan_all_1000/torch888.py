import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 3)
y = torch.sum(x, dim=1)
y = torch.sum(x, dim=1, keepdim=True)