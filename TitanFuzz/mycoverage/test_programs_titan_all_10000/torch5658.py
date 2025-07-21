import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3)
torch.nn.Softshrink(lambd=0.5)(x)
x = torch.randn(2, 3)
torch.nn.Softsign()(x)