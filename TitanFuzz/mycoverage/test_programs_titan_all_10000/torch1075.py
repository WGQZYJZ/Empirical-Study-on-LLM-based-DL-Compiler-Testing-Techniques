import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 3)
y = torch.as_strided(x, (2, 2), (2, 1))