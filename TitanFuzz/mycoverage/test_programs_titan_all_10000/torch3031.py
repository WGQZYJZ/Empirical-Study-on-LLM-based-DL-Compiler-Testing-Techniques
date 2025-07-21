import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4)
y = torch.special.logit(x)
x = torch.randn(4)
y = torch.special.expit(x)