import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(2, 2)
y = torch.special.logit(x)