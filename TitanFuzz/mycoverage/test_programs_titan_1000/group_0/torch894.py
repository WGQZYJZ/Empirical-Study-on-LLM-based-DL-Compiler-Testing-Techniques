import torch
from torch import nn
from torch.autograd import Variable
x1 = torch.randn(3, 3)
x2 = torch.randn(3, 3)
y = torch.concat([x1, x2], dim=0)