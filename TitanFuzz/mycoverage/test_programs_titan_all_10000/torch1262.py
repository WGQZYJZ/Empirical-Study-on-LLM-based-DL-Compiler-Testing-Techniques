import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(5, 5)
y = torch.special.logit(x)
z = torch.special.expit(y)
w = torch.sigmoid(x)
v = torch.logit(w)