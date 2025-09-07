import torch
from torch import nn
from torch.autograd import Variable

a = torch.randn(3, 3)
(q, r) = torch.geqrf(a)