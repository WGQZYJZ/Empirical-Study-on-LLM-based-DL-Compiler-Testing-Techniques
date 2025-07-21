import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(2, 3, 4)
(u, s, v) = torch.svd(a)