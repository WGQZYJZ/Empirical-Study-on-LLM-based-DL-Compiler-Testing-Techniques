import torch
from torch import nn
from torch.autograd import Variable

x = torch.ones(1)
y = torch.zeros(1)
torch.div(x, y)