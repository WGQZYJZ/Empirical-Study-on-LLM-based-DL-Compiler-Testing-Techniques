import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 4)
y = torch.masked_select(x, (x > 0.5))