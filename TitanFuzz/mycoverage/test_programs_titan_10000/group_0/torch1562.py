import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(1, 2, 3)
norm = torch.nn.LazyInstanceNorm1d(2)
y = norm(x)