import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 2)
y = torch.randn(1, 2)
output = torch.xlogy(x, y)