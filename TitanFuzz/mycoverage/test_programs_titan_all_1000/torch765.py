import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(4, 3)
v = torch.randn(3)
out = torch.mv(A, v)