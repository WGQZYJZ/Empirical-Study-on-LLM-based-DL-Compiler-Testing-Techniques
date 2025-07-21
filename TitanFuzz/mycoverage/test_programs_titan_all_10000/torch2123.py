import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 1)
y = torch.nn.functional.softplus(x)