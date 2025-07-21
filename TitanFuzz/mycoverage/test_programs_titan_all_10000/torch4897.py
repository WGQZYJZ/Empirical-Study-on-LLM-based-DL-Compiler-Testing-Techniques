import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(0, 3)
y = torch.arange(0, 3)
(xx, yy) = torch.meshgrid(x, y)