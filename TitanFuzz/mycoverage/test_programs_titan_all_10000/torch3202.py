import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(10)
y = torch.randn(10)
torch.xlogy(x, y)