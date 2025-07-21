import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(2, 3)
y = torch.angle(x)