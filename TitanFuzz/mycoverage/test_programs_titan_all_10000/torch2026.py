import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 2)
torch.nn.init.zeros_(input)