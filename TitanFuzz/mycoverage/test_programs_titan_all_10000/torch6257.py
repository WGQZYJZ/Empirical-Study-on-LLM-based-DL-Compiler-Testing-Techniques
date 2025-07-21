import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
torch.nn.init.eye_(input)