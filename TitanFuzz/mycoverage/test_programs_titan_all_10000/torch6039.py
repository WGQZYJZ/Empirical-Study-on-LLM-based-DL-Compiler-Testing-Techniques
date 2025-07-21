import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, requires_grad=True)
torch.special.logit(input, eps=None, out=None)