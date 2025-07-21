import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 4)
y = torch.transpose(x, 0, 1)