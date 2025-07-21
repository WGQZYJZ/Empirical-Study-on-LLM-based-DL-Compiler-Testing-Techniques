import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 3, 3)
torch.logit(input)
input = torch.randn(2, 3, 3, 3)
torch.logit(input, eps=1e-05)