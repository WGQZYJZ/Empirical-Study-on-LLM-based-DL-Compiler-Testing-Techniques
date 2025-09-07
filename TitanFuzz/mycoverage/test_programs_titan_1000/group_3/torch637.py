import torch
from torch import nn
from torch.autograd import Variable
input = torch.ones(1, 3, 3, 3)
torch.nn.init.kaiming_uniform_(input, a=0, mode='fan_in', nonlinearity='leaky_relu')