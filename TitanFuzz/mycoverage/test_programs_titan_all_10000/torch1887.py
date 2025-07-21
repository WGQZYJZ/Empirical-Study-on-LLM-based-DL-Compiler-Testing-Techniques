import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3, dtype=torch.float)
y = torch.neg(x)