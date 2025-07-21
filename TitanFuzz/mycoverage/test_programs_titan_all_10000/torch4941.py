import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 2)
y = torch.nn.ELU(alpha=1.0, inplace=False)(x)