import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 5)
y = torch.special.psi(x)