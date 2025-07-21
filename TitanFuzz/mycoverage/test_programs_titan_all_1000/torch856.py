import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(2, 3, 4)
torch.logcumsumexp(data, dim=1)
torch.logcumsumexp(data, dim=2)