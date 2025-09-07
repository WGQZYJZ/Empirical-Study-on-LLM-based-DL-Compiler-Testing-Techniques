import torch
from torch import nn
from torch.autograd import Variable

X = torch.randn(2, 3)
Y = torch.randn(2, 3)
Z = torch.copysign(X, Y)