import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
output = torch.logcumsumexp(input, dim=1)
output = torch.logcumsumexp(input, dim=0)
input = torch.randn(2, 3, 4)
output = torch.logcumsumexp(input, dim=1)
output = torch.logcumsumexp(input, dim=0)
output = torch.logcumsumexp(input, dim=2)