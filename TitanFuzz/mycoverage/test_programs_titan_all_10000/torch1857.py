import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3, 4)
(u, s, v) = torch.svd(x)