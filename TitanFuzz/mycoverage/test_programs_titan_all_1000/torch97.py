import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 2)
y = torch.nn.GELU()(x)