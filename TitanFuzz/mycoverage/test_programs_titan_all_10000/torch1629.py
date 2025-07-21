import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4, 5)
out = torch.nn.LPPool1d(2, 3, stride=2, ceil_mode=True)(input)