import torch
from torch import nn
from torch.autograd import Variable
x = torch.ones((3, 3))
torch.nn.init.constant_(x, 2)