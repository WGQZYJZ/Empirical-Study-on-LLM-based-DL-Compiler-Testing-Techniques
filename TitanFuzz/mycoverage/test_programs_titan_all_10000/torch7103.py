import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, 5)
torch.nn.init.normal_(input)