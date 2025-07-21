import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 5)
torch.nn.init.xavier_uniform_(x, gain=1.0)