import torch
from torch import nn
from torch.autograd import Variable
d = torch.randn(4, 4)
torch.nn.init.kaiming_normal_(d, a=0, mode='fan_in', nonlinearity='leaky_relu')
torch.nn.init.kaiming_normal_(d, a=0, mode='fan_in', nonlinearity='leaky_relu')