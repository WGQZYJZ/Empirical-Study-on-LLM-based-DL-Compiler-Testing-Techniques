import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
torch.special.logsumexp(input, dim=1)