import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 4, 5)
y = torch.moveaxis(x, 0, (- 1))
y = torch.moveaxis(x, 0, 1)
y = torch.moveaxis(x, 1, (- 1))
y = torch.moveaxis(x, (- 1), 0)