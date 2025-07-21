import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4, 4)
y = torch.special.logsumexp(x, dim=1, keepdim=True)
y = torch.logsumexp(x, dim=1, keepdim=True)
y = torch.max(x, dim=1, keepdim=True)