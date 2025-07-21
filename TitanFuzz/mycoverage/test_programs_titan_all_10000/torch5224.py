import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 5, requires_grad=True)
y = torch.special.logsumexp(x, dim=1, keepdim=True)