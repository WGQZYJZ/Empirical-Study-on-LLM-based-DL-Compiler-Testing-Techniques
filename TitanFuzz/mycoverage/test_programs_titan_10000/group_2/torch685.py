import torch
from torch import nn
from torch.autograd import Variable

a = torch.randn(1, 1)
b = torch.arccosh(a)
c = np.arccosh(a.numpy())