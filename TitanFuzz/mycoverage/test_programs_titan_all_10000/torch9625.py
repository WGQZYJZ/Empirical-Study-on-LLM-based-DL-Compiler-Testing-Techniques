import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(5)
softplus = torch.nn.Softplus()
y = softplus(x)