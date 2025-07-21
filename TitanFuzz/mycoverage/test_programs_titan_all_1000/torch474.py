import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1)
y = torch.nn.LogSigmoid()(x)
z = torch.sigmoid(x)
w = torch.log(z)