import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
output = torch.logsumexp(input, dim=1, keepdim=True)