import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4, 4)
(tau, q) = torch.geqrf(x)