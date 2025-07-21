import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(5, 3)
torch.nn.init.zeros_(x)