import torch
from torch import nn
from torch.autograd import Variable
x = torch.linspace(0, 1, steps=5)
y = torch.linspace(0, 1, steps=5)
(xx, yy) = torch.meshgrid(x, y)